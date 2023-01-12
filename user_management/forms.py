from django import forms
from .models import *


class HotelForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ['name','ppic']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'