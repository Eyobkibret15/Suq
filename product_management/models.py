from django.db import models
from django.utils import timezone

from user_management.models import UserProfile


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(ProductSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(ProductInventory, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.quantity)


class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    discount_present = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Discount, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='product_image', blank=True)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ShippingMethod(models.Model):
    free_delivery = models.BooleanField(default=False)
    free_return = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(ShippingMethod, self).save(*args, **kwargs)

    def __str__(self):
        if self.free_return and self.free_delivery:
            return 'Free delivery and return'
        elif self.free_delivery:
            return 'Free Delivery'
        elif self.free_return:
            return 'Free Return'
        else:
            return 'standard'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.FloatField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    subcategory_id = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    images = models.ManyToManyField(ProductImage)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.SET_NULL,null=True   )

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


