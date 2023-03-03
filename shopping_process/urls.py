from django.urls import path

from shopping_process.views import checkout,payment_summery,home,add_to_cart

urlpatterns = [
    path("", home, name="home"),
    path("checkout/", checkout, name="checkout"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("summery/", payment_summery, name="payment_summery"),
]