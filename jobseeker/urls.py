from django.urls import path
from .views import GetJobSeekerInfo ,UpdateJobSeekerInfo,GetAllJobSeekerInfo,GetJobSeekerInterview
# from .views

urlpatterns = [

    path('jobseeker-all/', GetAllJobSeekerInfo.as_view()),
    path('jobseeker-data/', GetJobSeekerInfo.as_view()),
    path('jobseeker-update/', UpdateJobSeekerInfo.as_view()),
    path('jobseeker-interviews/', GetJobSeekerInterview.as_view()),

    
 

    
]   