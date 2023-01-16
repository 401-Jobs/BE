# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,AbstractUser
# from rest_framework_simplejwt.tokens import RefreshToken

# class UserManger(BaseUserManager):
#     def create_user(self,username,email,password=None):
#         if username is None:
#             raise TypeError('users should have username')
#         if email is None:
#             raise TypeError('users shoud have email')
        
#         user=self.model(username=username,email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self,username,email,password):
#         user=self.create_user(
#             username,
#             email,
#             password
#         )
#         user.is_staff=True
#         user.is_superuser=True
#         user.is_active=True
#         user.save()
#         return user


# class User(AbstractUser):
#     username=models.CharField(max_length=255,unique=True)
#     email=models.EmailField(max_length=255,unique=True)
#     is_verified=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     is_company=models.BooleanField(default=False)

#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS = ['username']
#     # objects = UserManger()

#     def __str__(self) -> str:
#         return self.email
    
