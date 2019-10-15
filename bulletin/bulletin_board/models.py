import datetime

from django.db import models
from django.utils import timezone


class Car(models.Model):
   
    car_title = models.CharField( max_length=100, blank=True)
    pub_date = models.DateField( blank=True, null=True)
    price = models.FloatField( blank=True, null= True)
    seller = models.CharField( max_length=100, blank=True )
    phone = models.CharField( max_length=30, blank=True )
    car_description = models.TextField(blank=True)
    car_specs = models.TextField(blank=True)
    avito_item = models.CharField( max_length=100, blank=True)
    

    
       
