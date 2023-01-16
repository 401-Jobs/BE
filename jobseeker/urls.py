from django.urls import path
from .views import JobseekerView,JobSeekerDetails,UserMediarView,UserMediavDetails
urlpatterns = [
    path('jobseeker/', JobseekerView.as_view()),
    path('jobseeker/<int:pk>',JobSeekerDetails.as_view()),
    path('jobseekermedia/', UserMediarView.as_view()),
    path('jobseekermedia/<int:pk>',UserMediavDetails.as_view()),

    
]   