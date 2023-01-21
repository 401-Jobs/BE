from django.urls import path
#from .views import GetJobSeekerInfo ,UpdateJobSeekerInfo,GetAllJobSeekerInfo,GetJobSeekerInterview,UpdateInterviewConfirmation,GetJobSeekerRecentlyViewed
from .views import GetJobSeekerInfo , UpdatePersonalInfo , UpdateContact , UpdateEducation , CreateEducation
from .views import CreateWorkExperiance,UpdateWorkExperiance,UpdateUserMedia,UpdateClientDetails,GetJobSeekerInterview,UpdateInterviewConfirmation,GetJobSeekerRecentlyViewed,GetAllJobSeekerInfo
urlpatterns = [

    path('jobseeker-data/', GetJobSeekerInfo.as_view()),

    path('jobseeker-update-pf/', UpdatePersonalInfo.as_view()),

    path('jobseeker-update-contact/', UpdateContact.as_view()),

    path('jobseeker-create-education/', CreateEducation.as_view()),

    path('jobseeker-update-education/', UpdateEducation.as_view()),

    path('jobseeker-create-work/', CreateWorkExperiance.as_view()),

    path('jobseeker-update-work/', UpdateWorkExperiance.as_view()),

    path('jobseeker-update-media/', UpdateUserMedia.as_view()),

    path('jobseeker-update-details/', UpdateClientDetails.as_view()),

    path('jobseeker-interviews/', GetJobSeekerInterview.as_view()),

    path('jobseeker-update-interview/', UpdateInterviewConfirmation.as_view()),

    path('jobseeker-views/', GetJobSeekerRecentlyViewed.as_view()),

    path('jobseeker-all/', GetAllJobSeekerInfo.as_view()),
    
    

    
]   