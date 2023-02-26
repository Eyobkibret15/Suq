from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_management.forms import HotelForm
from user_management.models import Img

@api_view(['GET'])
def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def filter(request):
    return render(request, 'filter.html')


@api_view(['GET'])
def home2(request):
    return render(request, 'check.html')

@api_view(['GET','POST'])
def ppic(request):
    if request.method == 'POST':
        img = Img.objects.get(name='Awol')
        form = HotelForm(request.POST, request.FILES,instance=img)
        if form.is_valid():
            form.save()
            return Response(data='file uploaded successfully', status=201)
    else:
        form = HotelForm()
    return render(request, 'img.html', {'form': form})

@api_view(['GET'])
def checkout(request):
    return render(request, 'checkout.html')

@api_view(['GET'])
def payment_summery(request):
    return render(request, 'payment_summery.html    ')