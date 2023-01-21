from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_verified=models.BooleanField(default=False)  
    is_active=models.BooleanField(default=True)
    is_company=models.BooleanField(default=False)
    email=models.EmailField(max_length=255,unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username




class PersonalInfo(models.Model):
    firstName = models.CharField(max_length=200,null=True)
    lastName = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    lastName = models.CharField(max_length=200,null=True)
    jobtitle = models.CharField(max_length=200,null=True)
    yearsExperience = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=200,null=True)
    owner= models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.owner.username

class Contact(models.Model):
    email=models.CharField(max_length=255,null=True)
    phoneNumber = models.CharField(max_length=200,null=True)
    owner=models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.owner.username


class Education(models.Model):
    institute = models.CharField(max_length=200,null=True)
    degree = models.CharField(max_length=200,null=True)
    major = models.CharField(max_length=200,null=True)
    start = models.DateField( auto_now=False, auto_now_add=False,null=True)
    end = models.DateField(auto_now=False, auto_now_add=False,null=True)
    owner=models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.owner.username


class WorkExperiance(models.Model):
    title = models.CharField(max_length=200,null=True)
    subTitle = models.CharField(max_length=200,null=True)
    start = models.DateField( auto_now=False, auto_now_add=False,null=True)
    end = models.DateField(auto_now=False, auto_now_add=False,null=True)
    description=models.TextField(null=True)
    owner=models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.owner.username


class UserMedia(models.Model):
        video=models.FileField(upload_to='media/%y',null=True)
        image=models.FileField(upload_to='media/%y',null=True)
        owner=models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)


        def __str__(self) -> str:
            return "For  " + self.owner.username

class ClientDetails(models.Model):
    summary=models.TextField(null=True)
    skills=models.TextField(null=True)
    linkedin = models.CharField(max_length=250,null=True)
    github = models.CharField(max_length=250,null=True)
    porto = models.CharField(max_length=250,null=True)
    owner=models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return "For  " + self.owner.username




class Company(models.Model):
    owner = models.OneToOneField( CustomUser,on_delete=models.CASCADE, null=True, blank=True     )
    phone = models.CharField(max_length=200,null=True)
    company_name = models.CharField( max_length=150,null=True)
    company_website = models.URLField( max_length=350,null=True)
    company_address = models.CharField( max_length=150,null=True)
    about_company = models.TextField(null=True)
    logo = models.FileField(upload_to='media/%y',null=True)

    def __str__(self) -> str:
        return "For  " + self.owner.username

class RecentlyViewd(models.Model):
    jobseeker= models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    company= models.ForeignKey( Company,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return  self.company.company_name + " Viewd " + self.jobseeker.username

class Interview(models.Model):
    company= models.ForeignKey( Company,on_delete=models.CASCADE, null=True, blank=True     )
    jobseeker= models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True     )
    date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.TextField()
    isApproved_jobseeker = models.BooleanField(null=True)

    def __str__(self) -> str:
        return "For  " + self.company.owner.username + "  and  " + self.jobseeker.username

class ShortList(models.Model):
    company= models.ForeignKey( Company,on_delete=models.CASCADE, null=True, blank=True)
    jobseeker= models.ForeignKey( CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return "For  " + self.company.owner.username + "  and  " + self.jobseeker.owner.username
