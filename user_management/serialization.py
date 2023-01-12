from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user_management.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'