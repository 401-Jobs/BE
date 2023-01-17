from django.urls import path
from .views import RegisterView,VerifyEmail,LoginApiView,LogoutApiView,RequestPasswordResetEmail,SetNewPasswordAPIView,PasswordTokenCheckAPI

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginApiView.as_view(),name='login'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(),name='password-reset-complete'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('logout/', LogoutApiView.as_view(),name='logout'),
    path('eamil-verify/',VerifyEmail.as_view(),name='verify'),
]
