from django.db import models
from django.utils import timezone

from product_management.models import Product
from user_management.models import UserProfile


class PaymentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    amount = models.IntegerField()
    provider = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(PaymentDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order_id)


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(PaymentDetail, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.payment_id)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order_id)


# class ShoppingSession(models.Model):
#     id = models.CharField(max_length=100, primary_key=True)
#     user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(null=True,editable=False)
#     modified_at = models.DateTimeField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         """ On save, update timestamps """
#         if not self.id:
#             self.created_at = timezone.now()
#         self.modified_at = timezone.now()
#         return super(ShoppingSession, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.user_id.first_name + ' ' + self.user_id.last_name)


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user_id.first_name + ' ' + self.user_id.last_name + ' - ' + self.product_id.name )

