import json
import os

from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from user_management.forms import HotelForm, RegisterForm
from user_management.models import UserProfile
from user_management.serialization import UserSerializer
from django.contrib.auth.hashers import check_password


@api_view(['GET', 'POST'])
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        email = request.data['email']
        user = UserProfile.objects.filter(email=email)
        if user.exists() and check_password(request.data['password'], user.first().password):
            django_user = auth.authenticate(username=email, password=request.data['password'])
            auth.login(request, django_user)
            request.session['user_id'] = user.first().id  # Store user id in session
            print('sign in', user.first().id, request.session.get('user_id'))
            return redirect('home')
        else:
            return render(request, 'signin.html', context={'data': 'invalid user name or password'})


@api_view(['GET'])
def signout(request):
    logout(request)
    request.session['user_id'] = None
    return redirect('home')


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        request.data._mutable = True
        data = request.data
        data['telephone'] = data['countryCode'] + data['phone']
        user = UserSerializer(data=data)
        user_valid = user.is_valid()

        # check if the instance is valid to save
        try:
            my_instance = User(username=request.data['email'],is_superuser=True, is_staff=True)
            my_instance.set_password(request.data['password'])
            my_instance.full_clean()
        except ValidationError as e:
            return render(request, 'signup.html', context={'data': str(e)})
        except ValueError as e:
            return render(request, 'signup.html',
                          context={'data': 'Invalid password format or unknown hashing algorithm.'})
        if user_valid:
            user.save()
            my_instance.save()
            user_prof = UserProfile.objects.get(email=request.data['email'])
            django_user = auth.authenticate(username=request.data['email'], password=request.data['password'])
            auth.login(request, django_user)
            request.session['user_id'] = user_prof.id  # Store user id in session
            print('sign up', user_prof.id, request.session.get('user_id'))
            return redirect('home')
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
