from django.urls import path
from .views import RegisterView,VerifyEmail,LoginApiView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginApiView.as_view(),name='login'),
    path('eamil-verify/',VerifyEmail.as_view(),name='verify'),
]
