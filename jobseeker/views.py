from account.models import JobSeeker,ClientDetails,UserMedia,Interview
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from .serializer import InterviewsSerializer, MediaSerializer,ClientDetailsSerializer,JobSeekerSerializer
from .permissions import IsJobSeeker,IsOwner,IsOwnerForMedia    
from rest_framework import authentication
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response









class GetAllJobSeekerInfo(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        userInfo=JobSeeker.objects.all() 
        userMedia=UserMedia.objects.all() 
        userDetails=ClientDetails.objects.all() 
        
        s1 = JobSeekerSerializer(userInfo,many=True)
        s2 = MediaSerializer(userMedia,many=True)
        s3 = ClientDetailsSerializer(userDetails,many=True)

        data = {"userInfo" : s1.data , "userMedia" : s2.data , "userDetails" : s3.data}
        return JsonResponse (data,safe=False,status=200)

class GetJobSeekerInfo(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        userInfo=JobSeeker.objects.filter(owner=request.user) 
        userMedia=UserMedia.objects.filter(owner=request.user) 
        userDetails=ClientDetails.objects.filter(owner=request.user) 
        
        s1 = JobSeekerSerializer(userInfo,many=True)
        s2 = MediaSerializer(userMedia,many=True)
        s3 = ClientDetailsSerializer(userDetails,many=True)

        data = {"userInfo" : s1.data[0] , "userMedia" : s2.data[0] , "userDetails" : s3.data[0]}
        return JsonResponse (data,safe=False,status=200)

class UpdateJobSeekerInfo(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):

        userInfo=JobSeeker.objects.filter(owner=request.user) 
        userMedia=UserMedia.objects.filter(owner=request.user) 
        userDetails=ClientDetails.objects.filter(owner=request.user) 
        data = json.loads(request.body)
        print(data)
        userInfo.update(**data['userInfo'])
        userMedia.update(**data['userMedia'])
        userDetails.update(**data['userDetails'])
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetJobSeekerInterview(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = JobSeeker.objects.filter(owner = request.user)
        interviews=Interview.objects.filter(jobseeker=user[0]) 

        s1 = InterviewsSerializer(interviews,many=True)

        data = {"interviews" : s1.data }
        return JsonResponse (data,safe=False,status=200)