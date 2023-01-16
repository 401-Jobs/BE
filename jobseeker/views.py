from django.shortcuts import render
from account.models import JobSeeker,ClientDetails,UserMedia
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import MediaSerializer,ClientDetailsSerializer,JobSeekerSerializer
from .permissions import IsJobSeeker,IsOwner,IsOwnerForMedia    
# Create your views here.
class JobseekerView(ListCreateAPIView):
    def get_queryset(self):
 
        print(self.request.user)

        return JobSeeker.objects.filter(owner=self.request.user)
    serializer_class=JobSeekerSerializer
    permission_classes=[IsJobSeeker]

class JobSeekerDetails(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
 
        print(self.request.user)

        return JobSeeker.objects.filter(owner=self.request.user)
    serializer_class=JobSeekerSerializer
    permission_classes=[IsOwner]
class UserMediarView(ListCreateAPIView):
    queryset=UserMedia.objects.all()
    serializer_class=MediaSerializer
    permission_classes=[IsJobSeeker]

class UserMediavDetails(RetrieveUpdateDestroyAPIView):
    queryset=UserMedia.objects.all()
    serializer_class=MediaSerializer
    permission_classes=[IsOwnerForMedia]
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)

    # def put(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     # instance.delete_files()
    #     # instance.save()
    #     print(instance)
    #     return Response({"error": "Invalid credentials"}, status=401)