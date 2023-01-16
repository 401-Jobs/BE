from rest_framework import serializers
from account.models import UserMedia,JobSeeker,ClientDetails
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