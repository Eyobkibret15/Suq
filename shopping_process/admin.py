from django.contrib import admin

from shopping_process.models import PaymentDetail, OrderDetail, OrderItem, CartItem


@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'Payment Detail'


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'id', 'total', 'created_at', 'modified_at')
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'Order Detail'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'Order Item'


# @admin.register(ShoppingSession)
# class ShoppingSessionAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at','modified_at')
#     class Meta:
#         verbose_name = 'Shopping Session'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display =  ('user_id','product_id' ,'quantity', 'created_at','modified_at')
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'Cart Item'