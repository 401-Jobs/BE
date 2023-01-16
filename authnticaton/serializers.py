from rest_framework import serializers
from account.models import CustomUser as User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
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
        user=auth.authenticate(username=username,password=password)
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
