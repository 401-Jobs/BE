from django.shortcuts import render
from rest_framework import generics,status,views,permissions
from .serializers import RegisterSerializer,EmailVerification,LoginSerializer,LogoutSerializer,ResetPasswordEmailRequestSerializer,SetNewPasswordSerializer
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .renderers import UserJSONRenderer

import time

from account.models import CustomUser as User
from .utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
# import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication 

from account.models import JobSeeker,ClientDetails,UserMedia, Company , RecentlyViewd , Interview
from rest_framework.authtoken.models import Token


def init_new_jobseeker_user(user):
  seeker = JobSeeker(owner=user,        
    phone_number= None,
    github =   None,   
    protofolio=   None,
    IsSubscribed= None,
    experiance =  None,)

  seekerMedia = UserMedia(  video=None, 
    image=None, 
    owner=user, 
    CV=   None, )

  seekerDetails = ClientDetails( education=None,
    skilles=  None,
    country=  None,
    city=  None,
    jobTitle=  None,
    owner=    user,)


    

  seeker.save()
  seekerMedia.save()
  seekerDetails.save()

def init_new_company_user(user):
  print(user)
  company = Company(
    owner = user,
    phone = None,
    company_name = None,
    company_website = None,
    company_address = None,
    about_company = None,
    logo =  None
  )

  company.save()



class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    authentication_classes = (JWTAuthentication,)
    def post(self,request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        is_company = bool(request.data.get('is_company'))
        if not username or not email or not password:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username, email, password,is_company)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        init_new_jobseeker_user(user)
        init_new_company_user(user)
        token, created = Token.objects.get_or_create(user=user)

        #########################
        time.sleep(5)

        token=token
        current_site=get_current_site(request).domain
        relativeLink=reverse('verify')
        absurl='http://'+current_site+relativeLink+"?token="+str(token)
        email_body='Hi '+user.username+' use link below to verifiy\n'+absurl
        data={'email_body':email_body,'to_email':user.email,'email_subject':'Verify Your Email'}
        Util.send_email(data)
        #########################
        print(token)
        return Response({ "token": str(token)},status=status.HTTP_201_CREATED)
        # Return Redirect HostREact?Token={Token}
        # INside React Header Auth + Body Passwords

class VerifyEmail(views.APIView):
    serializer_class=EmailVerification

    token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY,description='Dscription',type=openapi.TYPE_STRING)
    # @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
      token=request.GET.get('token')
     
      try:
        token_obj = Token.objects.get(key=token)

        userobj = User.objects.get(email = token_obj.user.email)
        userobj.is_verified = True
        userobj.save()
        return Response({'email':'Successfuly activated'},status=status.HTTP_200_OK)
      except:
        return Response({'error':'invaild  token'},status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
      data={'request':request,'data':request.data}
      serializer=self.serializer_class(data=request.data)
      email=request.data['email']
      if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id))
            token=PasswordResetTokenGenerator().make_token(user)
            current_site=get_current_site(request=request).domain
            relativeLink=reverse('password-reset-confirm',kwargs={'uidb64':uidb64,'token':token})
            absurl='http://'+current_site+relativeLink
            email_body='Hi  use link below to reset your password\n'+absurl
            data={'email_body':email_body,'to_email':user.email,'email_subject':'reset your password'}
            Util.send_email(data)
            return Response({'success':"we have sent you link to reset your password"},status=status.HTTP_200_OK)
      else:
          return Response({'error':"email is not correct"},status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
              return Response({'error':'Token is not valid'})
            return Response({'success':True,'udb64':uidb64,'token':token,},status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                        return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

                    
            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)



class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

class LoginApiView(generics.GenericAPIView):
  serializer_class=LoginSerializer
  def post(self,request):
    user=request.data
    print("GOT POST REQUEST")
    serializer=self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

class LogoutApiView(generics.GenericAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class=LogoutSerializer
  def post(self,request):
    user=request.data
    serializer=self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    
