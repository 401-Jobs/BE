from django.shortcuts import render
from rest_framework import generics,status,views
from .serializers import RegisterSerializer,EmailVerification,LoginSerializer
from rest_framework.response import Response
from .renderers import UserJSONRenderer
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import CustomUser as User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
# Create your views here.
from account.models import JobSeeker,ClientDetails,UserMedia, Company , RecentlyViewd , Interview



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
    def post(self,request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data=serializer.data

        user=User.objects.get(email=user_data['email'])
        token=RefreshToken.for_user(user).access_token
        current_site=get_current_site(request).domain
        relativeLink=reverse('verify')
        absurl='http://'+current_site+relativeLink+"?token="+str(token)
        email_body='Hi '+user.username+' use link below to verifiy\n'+absurl
        data={'email_body':email_body,'to_email':user.email,'email_subject':'Verify Your Email'}
        Util.send_email(data)
        print(user_data)
        return Response(user_data,status=status.HTTP_201_CREATED)
        # Return Redirect HostREact?Token={Token}
        # INside React Header Auth + Body Passwords

class VerifyEmail(views.APIView):
    serializer_class=EmailVerification

    token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY,description='Dscription',type=openapi.TYPE_STRING)
    # @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
      token=request.GET.get('token')
      try:
        payload=jwt.decode (jwt=token,key=settings.SECRET_KEY,algorithms='HS256')
        user=User.objects.get(id=payload['user_id'])
        if not user.is_verified:
            user.is_verified=True
            user.save()
            if user.is_company == False: 
              init_new_jobseeker_user(user)
            else:
              init_new_company_user(user)
   
        # Return Rediriect to React verified Page
        return Response({'email':'Successfuly activated'},status=status.HTTP_200_OK)
      except jwt.ExpiredSignatureError  as identifier:
        return Response({'error':'Actiation  Expired'},status=status.HTTP_400_BAD_REQUEST)
      except jwt.exceptions.DecodeError as identifier:
         return Response({'error':'invaild  token'},status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(generics.GenericAPIView):
  serializer_class=LoginSerializer
  def post(self,request):
    user=request.data
    print("GOT POST REQUEST")
    serializer=self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data,status=status.HTTP_200_OK)