from django.urls import path

from shopping_process.views import home
from user_management.views import profile_pic, signin, signup, register,signout

urlpatterns = [
    path("upload_ppic/", profile_pic, name="ppic"),
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signout"),
    path("signup/", signup, name="signup"),
    path("register", register, name='register')
]
