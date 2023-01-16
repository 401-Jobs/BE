from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class CustomUser(AbstractUser):
    username=models.CharField(max_length=255,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_company=models.BooleanField(default=False)
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)

        }


class JobSeeker(models.Model):
    owner= models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    phone_number=models.CharField(max_length=200)
    github = models.URLField(max_length=200)
    protofolio=models.URLField(max_length=200)
    IsSubscribed=models.BooleanField()
        
class UserMedia(models.Model):
        video=models.FileField(upload_to='media/%y')
        image=models.FileField(upload_to='media/%y')
        owner=models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)
        CV=models.FileField(upload_to='media/%y')

class ClientDetails(models.Model):
    education=models.CharField(max_length=200)
    skilles=models.TextField()
    owner=models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)


class Company(models.Model):
    owner = models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True     )
    phone = models.CharField(max_length=200)
    company_name = models.CharField( max_length=150)
    company_website = models.URLField( max_length=350)
    company_address = models.CharField( max_length=150)
    about_company = models.TextField()
    logo = models.FileField(upload_to='media/%y')
