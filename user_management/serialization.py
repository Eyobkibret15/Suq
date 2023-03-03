from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user_management.models import UserProfile, CustomerRequest


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'