from django.urls import path

from shopping_process.views import home
from user_management.views import profile_pic

urlpatterns = [
    path("upload_ppic/", profile_pic, name="ppic"),
]