from django.db import models
from django.utils import timezone
from django_iban.fields import IBANField, SWIFTBICField

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Unidentified")]
    gender = models.CharField(choices=gender_choices, default="0", max_length=1)
    date_of_birth = models.DateField(blank=True, null=True)
    telephone = models.IntegerField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)  # You need to configure media in settings.py
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True,blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
class Img(models.Model):
    name = models.CharField(max_length=50)
    ppic = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)  # You need to configure media in settings.py

class UserAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    permanent_address = models.CharField(max_length=250)
    correspondence_address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(UserAddress, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_id.username

class UserPayment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=250)
    provider = models.CharField(max_length=250)
    account_number = IBANField()
    swift_bic = SWIFTBICField()
    expire = models.DateTimeField()
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(UserAddress, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_id.username