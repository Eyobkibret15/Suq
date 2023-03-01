from django.contrib import admin

from product_management.models import Product, ProductCategory, ProductInventory, Discount, ProductSubCategory, \
    ProductImage,ShippingMethod


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    filter_horizontal = ('images',)

    class Meta:
        verbose_name = 'Product'


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')

    class Meta:
        verbose_name = 'Shipping Method'


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')

    class Meta:
        verbose_name = 'Product Category'


@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')

    class Meta:
        verbose_name = 'Product SubCategory'


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')

    class Meta:
        verbose_name = 'Product Inventory'


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')

    class Meta:
        verbose_name = 'Discount'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')

    class Meta:
        verbose_name = 'Product Image'
