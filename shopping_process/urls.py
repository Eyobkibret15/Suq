from django.urls import path

from shopping_process.views import home, home2

urlpatterns = [
    path("", home, name="home"),
path("2", home2, name="home"),
]