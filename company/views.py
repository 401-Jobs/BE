from account.models import JobSeeker,ClientDetails,UserMedia,Interview,Company,RecentlyViewd,ShortList
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from .serializer import InterviewSerializer,CompanySerializer,ShortListSerializer
from rest_framework import authentication
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsCompany
from rest_framework import status
from rest_framework.response import Response
from jobseeker.serializer import JobSeekerSerializer ,MediaSerializer,ClientDetailsSerializer



class GetCompanyInfo(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        compayInfo=Company.objects.get(owner=request.user) 
        s1 = CompanySerializer(compayInfo,many=False)
        data = {"companyInfo" : s1.data}
        return JsonResponse (data,safe=False,status=200)

class UpdateCompanyInfo(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def put(self, request, *args, **kwargs):

        companyInfo=Company.objects.filter(owner=request.user) 
        data = json.loads(request.body)
        print(data)
        companyInfo.update(**data['companyInfo'])
        s1 = CompanySerializer(companyInfo,many=True)
        data = {"companyInfo" : s1.data[0] }
        return JsonResponse (data,safe=False,status=200)

class CreateInterview(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def post(self, request, *args, **kwargs):
        company = Company.objects.get(owner = request.user)
        data = json.loads(request.body)
        jobseeker= JobSeeker.objects.get(id= data["id"])
        
        interview = Interview(
            company= company,
            jobseeker= jobseeker,
            date =data["date"] ,
            notes = data["notes"] ,
            isApproved_jobseeker=None
        )

        interview.save()
        allinterviews=Interview.objects.filter(company=company)

        s2 = InterviewSerializer(allinterviews,many=True)
        data = {"interviews" : s2.data }
        return JsonResponse (data,safe=False,status=200)




class CreateRecentlyViewed(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def post(self, request, *args, **kwargs):
        company = Company.objects.get(owner = request.user)
        data = json.loads(request.body)
        jobseeker = JobSeeker.objects.get(id = data['id'])
        recentlyViewd = RecentlyViewd(
            company= company,
            jobseeker= jobseeker,
           
        )
        recentlyViewd.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class CreateShortlist(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def post(self, request, *args, **kwargs):
        company = Company.objects.get(owner = request.user)
        data = json.loads(request.body)
        jobseeker = JobSeeker.objects.get(id = data['id'])
        shortList = ShortList(
            company= company,
            jobseeker= jobseeker,
           
        )
        shortList.save()
        userInfo=JobSeeker.objects.filter(id=data["id"]) 
        userMedia=UserMedia.objects.filter(id=data["id"]) 
        userDetails=ClientDetails.objects.filter(id=data["id"]) 
        s1 = JobSeekerSerializer(userInfo,many=True)
        s2 = MediaSerializer(userMedia,many=True)
        s3 = ClientDetailsSerializer(userDetails,many=True)
        print(s3.data)
        data = {"userInfo" : s1.data[0] , "userMedia" : s2.data[0] }
        return JsonResponse (data,safe=False,status=200)

class GetShortlist(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def get(self, request, *args, **kwargs):  
        company = Company.objects.get(owner = request.user)
        shortlist = ShortList.objects.filter(company = company) 
        jobSeekers=[]
        medias=[]
        details=[]
        for i in shortlist:
            owner=i.jobseeker.owner
            clientDetails=ClientDetails.objects.get(owner=owner)
            media=UserMedia.objects.get(owner=owner)
            medias.append(media)
            details.append(clientDetails)
            jobSeekers.append(i.jobseeker)
            

        
        s1=JobSeekerSerializer(jobSeekers,many=True)
        s2 = MediaSerializer(medias,many=True)
        s3 = ClientDetailsSerializer(details,many=True)
        
        data = {"userInfo" : s1.data[0] , "userMedia" : s2.data[0] , "userDetails" : s3.data[0]}
        return JsonResponse (data,safe=False,status=200)

class DeleteShortlist(APIView):
    permission_classes=[IsCompany,IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        jobseeker=JobSeeker.objects.filter(id=data["id"])   
        shortlist=ShortList.objects.get(jobseeker=jobseeker[0])
        shortlist.delete()
        return Response(status=status.HTTP_200_OK)


        
