from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user_management.models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'