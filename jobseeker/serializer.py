from rest_framework import serializers
from account.models import Interview, UserMedia,JobSeeker,ClientDetails
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