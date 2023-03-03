from django.db import models
from django.utils import timezone
from django_iban.fields import IBANField, SWIFTBICField
from django.contrib.auth.hashers import make_password


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    gender = models.CharField(choices=gender_choices, max_length=1)
    date_of_birth = models.DateField(blank=True, null=True)
    telephone = models.IntegerField(unique=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics',
                                        blank=True)  # You need to configure media in settings.py
    created_at = models.DateTimeField(editable=False)
    rating = models.FloatField(null=True, blank=True, max_length=5)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        self.password = make_password(self.password)
        return super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Img(models.Model):
    name = models.CharField(max_length=50)
    ppic = models.ImageField(default='default.jpg', upload_to='profile_pics',
                             blank=True)  # You need to configure media in settings.py


class UserAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
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
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
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


class CustomerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    subject = models.CharField(max_length=10000)
    message = models.TextField()
    attach_file = models.ImageField(default='default.jpg', upload_to='contact_form',
                                        blank=True)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(CustomerRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject