from django.urls import path

from shopping_process.views import checkout,order,home,add_to_cart,get_cart,payment_summery

urlpatterns = [
    path("", home, name="home"),
    path("checkout/", checkout, name="checkout"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("get-cart/", get_cart, name="get_cart"),
    path("submit-checkout/", order, name="submit_checkout"),
    path("checkout/fsummery/<int:order_id>",payment_summery, name = 'payment_summery')
]