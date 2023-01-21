from .permissions import IsJobSeeker,IsOwner  
from rest_framework import authentication
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response


from .serializer import *
from accounts.models import CustomUser, PersonalInfo,Contact,Education,WorkExperiance,UserMedia,ClientDetails,Interview,Company,RecentlyViewd



class GetJobSeekerInfo(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        userInfo=PersonalInfo.objects.filter(owner=request.user) 
        userContact=Contact.objects.filter(owner=request.user) 
        userEducation=Education.objects.filter(owner=request.user) 
        userWork=WorkExperiance.objects.filter(owner=request.user) 
        userMedia=UserMedia.objects.filter(owner=request.user) 
        userDetails=ClientDetails.objects.filter(owner=request.user) 
        
        s1 = PersonalInfoSerializer(userInfo,many=True)
        s2 = ContactSerializer(userContact,many=True)
        s3 = EducationSerializer(userEducation,many=True)
        s4 = WorkExperianceSerializer(userWork,many=True)
        s5 = UserMediaSerializer(userMedia,many=True)
        s6 = ClientDetailsSerializer(userDetails,many=True)


        data = {"userInfo" : s1.data[0] , "userContact" : s2.data[0] , "userEducation" : s3.data
        , "userWork": s4.data, "userMedia" : s5.data[0] , "userDetails" : s6.data[0] }
        return JsonResponse (data,safe=False,status=200)

    
class UpdatePersonalInfo(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):
        try:
            if "userInfo" not in str(request.body):
                return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            data = json.loads(request.body)
            if data.get("userInfo") == None:
                return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            userInfo=PersonalInfo.objects.filter(owner=request.user) 
            userInfo.update(**data['userInfo'])
            return JsonResponse (data,safe=False,status=200)
        except:
            return Response({'error':"Somthing went wrong"},status=status.HTTP_400_BAD_REQUEST)




class UpdateContact(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):
        if "userContact" not in str(request.body):
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(request.body)

        
        if data.get("userContact") == None:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        userContact=Contact.objects.filter(owner=request.user) 
        userContact.update(**data['userContact'])
        return JsonResponse (data,safe=False,status=200)


class CreateEducation(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if "userEducation" not in str(request.body):
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(request.body)
        if data.get("userEducation") == None:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        print(data['userEducation'])
        userEducation=Education(owner = request.user,**data['userEducation'])
        userEducation.save()
        return Response({"message" : "created "},status=status.HTTP_201_CREATED)

class UpdateEducation(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):
        if "userEducation" not in str(request.body):
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(request.body)

        if data.get("userEducation") == None:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        id = data['userEducation']['id']
        userEducation=Education.objects.filter(id=id) 
        userEducation.update(**data['userEducation'])
        return JsonResponse (data,safe=False,status=200)



class CreateWorkExperiance(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:

            if "userWork" not in str(request.body):
                
                return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            data = json.loads(request.body)
            if data.get("userWork") == None:
                return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            print(data['userWork'])
            userWork=WorkExperiance(owner = request.user,**data['userWork'])
            userWork.save()
            return Response({"message" : "created "},status=status.HTTP_201_CREATED)
        except:
            return Response({'error':"Somthing went wrong"},status=status.HTTP_400_BAD_REQUEST)


class UpdateWorkExperiance(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):
        if "userWork" not in str(request.body):
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(request.body)

        if data.get("userWork") == None:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
        id = data['userWork']['id']
        userWork=WorkExperiance.objects.filter(id=id) 
        userWork.update(**data['userWork'])
        return JsonResponse (data,safe=False,status=200)


        

from django.core.files import File
class UpdateUserMedia(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):
        
        try :
            image = request.FILES['image']
            video = request.FILES['video']
            userWork=UserMedia.objects.get(owner=request.user) 
            userWork.image = File(image)
            userWork.video = File(video)
            userWork.save()
            return Response({"message" : "updated "},status=status.HTTP_201_CREATED)
        except:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            userDetails=ClientDetails.objects.filter(owner=request.user) 

class UpdateClientDetails(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):
        try:
                
            if "userDetails" not in str(request.body):
                return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            data = json.loads(request.body)
            if data.get("userDetails") == None:
                return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)
            userDetails=ClientDetails.objects.filter(owner=request.user) 
            userDetails.update(**data['userDetails'])
            return JsonResponse (data,safe=False,status=200)
        except:
            return Response({'error':"Somthing went wrong"},status=status.HTTP_400_BAD_REQUEST)
            



class GetJobSeekerInterview(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:

            interviews=Interview.objects.filter(jobseeker=request.user,isApproved_jobseeker=None)
            companies = []

            for interview in interviews:
                companies.append(interview.company)

            s1 = InterviewsSerializer(interviews,many=True)
            s2 = CompanySerializer(companies,many=True)

            
            data = {"interviews" : s1.data , "companies" : s2.data }
            return JsonResponse (data,safe=False,status=200)
        except:
            return Response({'error':"Somthing went wrong"},status=status.HTTP_400_BAD_REQUEST)


class UpdateInterviewConfirmation(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def put(self, request, *args, **kwargs):


        try:
            data = json.loads(request.body)
            interview=Interview.objects.get(id=data['id'])  # GETS YOU THE INTERVIEw QUERYSET
    
            interview.isApproved_jobseeker = data['status'] # FIELDS OF INTERVIEW QUERYSET

            interview.save() # SAVE

            s1 = InterviewsSerializer(interview,many=False) # JSON ONLY
            data = {"interview" : s1.data }
            return JsonResponse (data,safe=False,status=200)
        except:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)


class GetJobSeekerRecentlyViewed(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            allviews = RecentlyViewd.objects.filter(jobseeker = request.user).order_by('id').latest('id') # Array
            s1 = CompanySerializer(allviews.company,many=False)
            data = {"View" : s1.data }
            return JsonResponse (data,safe=False,status=200)
        except:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)


class GetAllJobSeekerInfo(APIView):
    permission_classes=[IsJobSeeker,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
                
            userInfo=PersonalInfo.objects.all() 
            userContact=Contact.objects.all() 
            userEducation=Education.objects.all() 
            userWork=WorkExperiance.objects.all() 
            userMedia=UserMedia.objects.all() 
            userDetails=ClientDetails.objects.all() 
            
            s1 = PersonalInfoSerializer(userInfo,many=True)
            s2 = ContactSerializer(userContact,many=True)
            s3 = EducationSerializer(userEducation,many=True)
            s4 = WorkExperianceSerializer(userWork,many=True)
            s5 = UserMediaSerializer(userMedia,many=True)
            s6 = ClientDetailsSerializer(userDetails,many=True)


            data = {"userInfo" : s1.data , "userContact" : s2.data , "userEducation" : s3.data
            , "userWork": s4.data, "userMedia" : s5.data , "userDetails" : s6.data }
            return JsonResponse (data,safe=False,status=200)
        except:
            return Response({'error':"Missing Data"},status=status.HTTP_400_BAD_REQUEST)