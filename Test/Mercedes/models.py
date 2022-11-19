from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class carshowroom(models.Model):
    brand = models.CharField(max_length=210)
    provider = models.CharField(max_length=200)
    country_producent = models.CountryField()
    price = models.DecimalField(max_digits=10, decimal_places=3, )
    feature = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

class Provider(models.Model):
    company_name = models.CharField(max_length=100)
    founder = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.company_name
