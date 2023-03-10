from django.contrib import admin

from user_management.models import UserProfile, UserAddress, UserPayment, CustomerRequest, Img


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'Users'
@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    # readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'img'


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'User Address'

@admin.register(CustomerRequest)
class CustomerRewquestAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'Customer Request'

@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','modified_at')
    class Meta:
        verbose_name = 'User Payment'