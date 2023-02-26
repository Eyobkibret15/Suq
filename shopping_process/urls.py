from django.urls import path

from shopping_process.views import checkout,payment_summery,home

urlpatterns = [
    path("", home, name="home"),
    path("checkout/", checkout, name="checkout"),
    path("summery/", payment_summery, name="payment_summery"),
]