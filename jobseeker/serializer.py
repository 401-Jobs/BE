from rest_framework import serializers
from accounts.models import PersonalInfo,Contact,Education,WorkExperiance,UserMedia,ClientDetails,UserMedia,Interview,Company,RecentlyViewd

class InterviewsSerializer(serializers.ModelSerializer):
        class Meta:
            model= Interview
            fields='__all__'

class PersonalInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model= PersonalInfo
            fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
        class Meta:
            model= Contact
            fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
        class Meta:
            model= Education
            fields='__all__'

class WorkExperianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperiance
        fields='__all__'

class UserMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMedia
        fields='__all__'

class ClientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDetails
        fields='__all__'

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields='__all__'

class RecentlyViewdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentlyViewd
        fields='__all__'


        