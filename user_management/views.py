import json
import os

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from user_management.forms import HotelForm, RegisterForm
from user_management.models import User
from user_management.serialization import UserSerializer
from django.contrib.auth.hashers import check_password


@api_view(['GET', 'POST'])
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        email = request.data['email']
        user = User.objects.filter(email=email)
        if user.exists() and check_password(request.data['password'], user.first().password):
            return redirect('home')
        else:
            return render(request, 'signin.html', context={'data': 'invalid user name or password'})


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        request.data._mutable = True
        data = request.data
        data['telephone'] = data['countryCode'] + data['phone']
        user = UserSerializer(data=data)
        if user.is_valid():
            user.save()
            return render(request, 'index.html')
        else:
            data = json.dumps(user.errors)
            return render(request, 'signup.html', context={'data': data})


@api_view(['POST'])
def profile_pic(request: Request):
    form = HotelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return Response(data='file uploaded successfully', status=201)
    else:
        form = HotelForm()
    return render(request, 'img.html', {'form': form})


@api_view(['POST'])
def register(request: Request):
    pass
