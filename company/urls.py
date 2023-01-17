from django.urls import path
from .views import DeleteShortlist,CreateInterview,GetCompanyInfo,UpdateCompanyInfo,CreateRecentlyViewed,CreateShortlist,GetShortlist
urlpatterns = [

    path('create-interview/', CreateInterview.as_view()),
    path('get-company-info/', GetCompanyInfo.as_view()),
    path('update-company-info/', UpdateCompanyInfo.as_view()),
    path('create-view/', CreateRecentlyViewed.as_view()),
    path('create-shortlist/', CreateShortlist.as_view()),
    path('get-shortlist/', GetShortlist.as_view()),
    path('delete-shortlist/', DeleteShortlist.as_view()),





    
 

    
]   