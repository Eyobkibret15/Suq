import decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_management.forms import HotelForm
from user_management.models import Img, UserProfile
from shopping_process.models import CartItem, OrderItem,OrderDetail, Product
from product_management.models import Product


@api_view(['GET'])
def home(request):
    session_id = request.session.session_key
    user_id = request.session.get('user_id')
    context = {'user_id': user_id}
    return render(request, 'index.html', context)


@api_view(['GET'])
def filter(request):
    return render(request, 'filter.html')


@api_view(['GET'])
def home2(request):
    return render(request, 'check.html')


@api_view(['GET', 'POST'])
def ppic(request):
    if request.method == 'POST':
        img = Img.objects.get(name='Awol')
        form = HotelForm(request.POST, request.FILES, instance=img)
        if form.is_valid():
            form.save()
            return Response(data='file uploaded successfully', status=201)
    else:
        form = HotelForm()
    return render(request, 'img.html', {'form': form})


@api_view(['GET'])
def checkout(request):
    user_id = request.session.get('user_id')
    if user_id:
        context = {'user_id': user_id}
        return render(request, 'checkout.html', context)
    else:
        return render(request, 'signin.html')


@api_view(['GET'])
def order(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = UserProfile.objects.get(id=user_id)
        data = dict(request.GET)
        ex_data = {}
        for k,v in data.items():
            if k == 'total_price':
                continue
            else:
                ex_data[k.split("[")[0]] = {}
        for k, v in data.items():
            if k == 'total_price':
                ex_data['total_price'] = v[0]
            else:
                ex_data[k.split("[")[0]][k.split("[")[1].split("]")[0]] = v[0]
        order_detail = OrderDetail.objects.create(user_id=user, total=ex_data['total_price'])
        for k,v in ex_data.items():
            if not k == 'total_price':
                name = ex_data[k]['name']
                quant = ex_data[k]['quantity']
                product = Product.objects.get(name=name)
                order_item = OrderItem.objects.create(order_id=order_detail,product_id=product,quantity=quant)
        return Response(data={'order_id':order_detail.id},status=201)
    else:
        return render(request, 'signin.html')


@api_view(['GET'])
def get_cart(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return Response(status=400)
    user = UserProfile.objects.get(id=user_id)
    carts = CartItem.objects.filter(user_id=user)
    data = {}
    total_quan = 0
    total_cost = 0
    for cart in carts:
        discount = cart.product_id.discount_id
        price = cart.product_id.price
        if discount:
            cost = decimal.Decimal(price) - (discount.discount_present / 100) * decimal.Decimal(price)
        else:
            cost = price
        quan = cart.quantity
        total_quan += quan
        total_cost +=decimal.Decimal(cost) * quan
        data[cart.product_id.name] = {'quantity': quan, 'cost': cost}
    data['quantity'] = total_quan
    data['cost'] = total_cost
    return Response(data=data, status=200)


@api_view(['GET'])
def add_to_cart(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return Response(status=400)
    user = UserProfile.objects.get(id=user_id)
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart = CartItem.objects.get_or_create(user_id=user,product_id=product,quantity=1)
    return Response(status=201)

@api_view(['GET'])
def payment_summery(request,order_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return Response(status=400)
    user = UserProfile.objects.get(id=user_id)
    return render(request, 'payment_summery.html',context={'order_id': order_id,'user_id':user_id})