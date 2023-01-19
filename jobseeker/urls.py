from django.urls import path
from .views import GetJobSeekerInfo ,UpdateJobSeekerInfo,GetAllJobSeekerInfo,GetJobSeekerInterview,UpdateInterviewConfirmation,GetJobSeekerRecentlyViewed
# from .views

urlpatterns = [

    path('jobseeker-all/', GetAllJobSeekerInfo.as_view()),
    path('jobseeker-data/', GetJobSeekerInfo.as_view()),
    path('jobseeker-update/', UpdateJobSeekerInfo.as_view()),
    path('jobseeker-interviews/', GetJobSeekerInterview.as_view()),
    path('jobseeker-update-interview/', UpdateInterviewConfirmation.as_view()),
    path('jobseeker-views/', GetJobSeekerRecentlyViewed.as_view()),
    
 

    
]   