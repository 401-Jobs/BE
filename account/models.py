from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    is_company=models.BooleanField(default=False)


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
