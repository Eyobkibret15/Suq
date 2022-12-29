from django.urls import path

from product_management.views import categories, product

urlpatterns = [
    path("", product, name="products"),
    path("categories/", categories, name="categories"),
]