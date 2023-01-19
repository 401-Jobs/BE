from rest_framework import serializers
from accounts.models import Company, Interview,ShortList
class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model= Company
            fields='__all__'

class InterviewSerializer(serializers.ModelSerializer):
        class Meta:
            model= Interview
            fields='__all__'

class ShortListSerializer(serializers.ModelSerializer):
        class Meta:
            model= ShortList
            fields='__all__'