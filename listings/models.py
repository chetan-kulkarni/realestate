from django.db import models
from realtors.models import Realtor
from datetime import datetime

class Listing(models.Model):
    realtors = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) # black true means optional
    price = models.CharField(max_length=20)
    bedrooms = models.CharField(max_length=100)
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d') # save the phots as datewise
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    for_rent_only = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True) # gives current date

    def __str__(self):
        return self.title
