from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_management.forms import HotelForm
from product_management.models import ProductCategory, Product


@api_view(['GET'])
def home(request):
    return render(request, 'index.html')


@api_view(['GET'])
def product(request):
    products = Product.objects.filter(active=True)
    data = {}
    for product in products:
        print(product.name)
        image_ids = product.images.all()
        images = []
        for image_id in image_ids:
            images.append(str(image_id.image))
        quantity = product.inventory_id
        if quantity: quantity = quantity.quantity
        discount = product.discount_id
        if discount: discount = product.discount_id.discount_present
        price = product.price
        description = product.description
        data[product.name] = {'images': images, 'discount': discount, 'price': price,
                              'description': description, 'quantity': quantity}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def categories(request):
    categories = ProductCategory.objects.all()
    data = {'name': []}
    for cate in categories:
        data['name'].append(cate.name)
    return Response(data=data, status=status.HTTP_200_OK)
