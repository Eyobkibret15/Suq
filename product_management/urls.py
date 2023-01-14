from django.urls import path

from product_management.views import filters, product,product_detail,product_page

urlpatterns = [
    path("", product, name="products"),
    path("<int:id>", product_page, name="product_page"),
    path("detail/<int:id>", product_detail, name="product_detail"),
    path("filters/", filters , name="filters"),
]