from django.urls import path

from product_management.views import filters, product

urlpatterns = [
    path("", product, name="products"),
    path("filters/", filters , name="filters"),
]