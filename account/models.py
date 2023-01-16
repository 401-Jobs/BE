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
    phone_number=models.CharField(max_length=200,null=True)
    github = models.URLField(max_length=200,null=True)
    protofolio=models.URLField(max_length=200,null=True)
    IsSubscribed=models.BooleanField(default=False,null=True)
    experiance = models.IntegerField(default=0,null=True)



class UserMedia(models.Model):
        video=models.FileField(upload_to='media/%y',null=True)
        image=models.FileField(upload_to='media/%y',null=True)
        owner=models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)
        CV=models.FileField(upload_to='media/%y',null=True)


class ClientDetails(models.Model):
    education=models.CharField(max_length=200, null=True)
    skilles=models.TextField(null=True)
    country = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    jobTitle = models.CharField(max_length=200,null=True)
    owner=models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)



class Company(models.Model):
    owner = models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True     )
    phone = models.CharField(max_length=200,null=True)
    company_name = models.CharField( max_length=150,null=True)
    company_website = models.URLField( max_length=350,null=True)
    company_address = models.CharField( max_length=150,null=True)
    about_company = models.TextField(null=True)
    logo = models.FileField(upload_to='media/%y',null=True)


class Interview(models.Model):
    company= models.ForeignKey( Company,on_delete=models.CASCADE, null=True, blank=True     )
    jobseeker= models.ForeignKey( JobSeeker,on_delete=models.CASCADE, null=True, blank=True     )
    date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.TextField()
    isApproved_jobseeker = models.BooleanField(null=True)


class ShortList(models.Model):
    company= models.ForeignKey( Company,on_delete=models.CASCADE, null=True, blank=True)
    jobseeker= models.ForeignKey( JobSeeker,on_delete=models.CASCADE, null=True, blank=True)
