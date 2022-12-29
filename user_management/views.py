import os

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from user_management.forms import HotelForm
from user_management.models import User


@api_view(['POST'])
def profile_pic(request:Request):
    form = HotelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return Response(data='file uploaded successfully',status=201)
    else:
        form = HotelForm()
    return render(request, 'img.html', {'form': form})




