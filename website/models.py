from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.

class Profile(models.Model):
    profile_name = models.CharField(max_length=50, blank=True)
    home = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    services = models.CharField(max_length=50)
    works = models.CharField(max_length=50)
    clients = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    intro_big_text = models.TextField(max_length=200, blank=True)
    intro_button = models.CharField(max_length=50)
    about_title = models.CharField(max_length=100, blank=True)
    about_text = models.TextField(max_length=500, blank=True)

    works_title = models.CharField(max_length=200, blank=True)
    works_text = models.TextField(max_length=500, blank=True)

    services_title = models.CharField(max_length=100, blank=True)
    services_text = models.TextField(max_length=500, blank=True)

    clients_title = models.CharField(max_length=100, blank=True)
    clients_text = models.TextField(max_length=500, blank=True)

    contact_title = models.CharField(max_length=100, blank=True)
    contact_text = models.CharField(max_length=500, blank=True)
    contact_button = models.CharField(max_length=50, blank=True)


    address_title = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=500, blank=True)

    email_title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    phone_title = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField(blank=True)

    class Meta:
        verbose_name = "profile"

    def __str__(self):
        return self.profile_name


class Work(models.Model):
    work_name = models.CharField(max_length=50)
    work_kind = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='work/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "work"

    def __str__(self):
        return self.work_name














