from django.urls import path
from .views import RegisterView,VerifyEmail,LoginApiView,LogoutApiView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginApiView.as_view(),name='login'),
    path('logout/', LogoutApiView.as_view(),name='logout'),
    path('eamil-verify/',VerifyEmail.as_view(),name='verify'),
]
