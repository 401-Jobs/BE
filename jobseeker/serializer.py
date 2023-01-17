from rest_framework import serializers
from account.models import Company, Interview, RecentlyViewd, UserMedia,JobSeeker,ClientDetails
class MediaSerializer(serializers.ModelSerializer):
        class Meta:
            model= UserMedia
            fields='__all__'
class JobSeekerSerializer(serializers.ModelSerializer):
        class Meta:
            model= JobSeeker
            fields='__all__'
class ClientDetailsSerializer(serializers.ModelSerializer):
        class Meta:
            model= ClientDetails
            fields='__all__'

class InterviewsSerializer(serializers.ModelSerializer):
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


        