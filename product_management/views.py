from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_management.forms import HotelForm
from product_management.models import ProductCategory, Product


@api_view(['GET'])
def home(request):
    return render(request, 'check.html')

@api_view(['GET'])
def product_page(request, id):
    user_id = request.session.get('user_id')
    if user_id:
        context = {'user_id': user_id}
        return render(request, 'product_detail.html',context)
    else:
        return render(request, 'signin.html')

@api_view(['GET'])
def product_detail(request, id: int):
    user_id = request.session.get('user_id')
    if user_id:
        product = Product.objects.get(active=True, id=id)
        data = {}
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
        categories = product.subcategory_id.category_id.name
        subcategories = product.subcategory_id.name
        rating = product.owner.rating
        id = product.id
        name = product.name
        data = {'id': id, 'name': name, 'images': images, 'discount': discount, 'price': price,
                'subcategories': subcategories,
                'description': description, 'quantity': quantity, 'categories': categories,
                'rating': rating}
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        return render(request, 'signin.html')


@api_view(['GET'])
def product(request):
    products = Product.objects.filter(active=True)
    data = {}
    count = 1
    for product in products:
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
        categories = product.subcategory_id.category_id.name
        subcategories = product.subcategory_id.name
        rating = product.owner.rating
        popularity = count
        shipping = product.shipping_method
        if shipping.free_return and shipping.free_delivery:
            shipping_option = 'F-D-R'
        elif shipping.free_delivery:
            shipping_option = 'F-D'
        elif shipping.free_return:
            shipping_option = 'F-R'
        else:
            shipping_option = 'ST'
        count += 1
        id = product.id
        data[product.name] = {'id': id, 'shipping_option': shipping_option, 'popularity': popularity, 'images': images,
                              'discount': discount, 'price': price, 'subcategories': subcategories,
                              'description': description, 'quantity': quantity, 'categories': categories,
                              'rating': rating}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def filters(request):
    categories = ProductCategory.objects.all()
    data = {'categories': {}}
    for cate in categories:
        data['categories'][cate.name] = cate.name
        sub_categories = cate.productsubcategory_set.all()
        data['categories'][cate.name] = {'subcategories': []}
        for subccate in sub_categories:
            data['categories'][cate.name]['subcategories'].append(subccate.name)
    return Response(data=data, status=status.HTTP_200_OK)
