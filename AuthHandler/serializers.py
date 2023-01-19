from rest_framework import serializers
from accounts.models import CustomUser as User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    
    class Meta:
        model=User
        fields=['email','username','password',"is_company"]
    def validate(self, attrs):
        email=attrs.get('email', '')
        username=attrs.get('username', '')
        is_company = attrs.get('is_company', '')
        print("INSIDE SERALIZERS")
        print(is_company)
        if not username.isalnum():
            raise serializers.ValidationError('usre name should only have a char')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerification(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields=['token']

class LoginSerializer(serializers.ModelSerializer[User]):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    username=serializers.CharField(max_length=255,min_length=3,read_only=True)
    tokens=serializers.CharField(max_length=68,min_length=6,read_only=True)


    class Meta:
        model=User
        fields=['email','password','username','tokens']
    def validate(self, attrs):
        username=attrs.get('username', '')
        email=attrs.get('email', '')
        password=attrs.get('password', '')
        print(email)
        print(username,password)
        user=auth.authenticate(email=email,password=password)
        print(user)
       
        if  user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')   
        if not user.is_active:
            raise serializers.ValidationError('Account disabled')
        if not user.is_verified:
            raise serializers.ValidationError('Email is not vaerified')  

        return {
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens
         }     

       

        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer):
    
    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    refresh_token=serializers.CharField()
    def validate(self, attrs):
        self.token=attrs['refresh_token']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']
    

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']
    
    def validate(self, attrs):
        try:
            password=attrs.get('password')
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')
            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('the reset link is invalid',401)
            user.set_password(password)
            user.save()
            return(user)
        except Exception as e:
            raise AuthenticationFailed('the reset link is invalid',401)



        return super().validate(attrs)