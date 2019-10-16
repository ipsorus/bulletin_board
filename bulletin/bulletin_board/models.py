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
    avito_item = models.CharField( max_length=100, blank=True)
    car_brand = models.CharField( max_length=100, blank=True)
    car_model = models.CharField( max_length=100, blank=True)
    car_generation = models.CharField( max_length=100, blank=True)
    modif = models.CharField( max_length=100, blank=True)
    year_of_manufacture = models.IntegerField(blank=True, null=True)
    car_mileage = models.IntegerField(blank=True, null=True)
    condition = models.CharField( max_length=100, blank=True)
    owners = models.IntegerField(blank=True, null=True)
    vin_number = models.CharField( max_length=100, blank=True)
    type_chassis = models.CharField( max_length=100, blank=True)
    doors = models.IntegerField(blank=True, null=True)
    engine_type = models.CharField( max_length=100, blank=True)
    transmission = models.CharField( max_length=100, blank=True)
    drive = models.CharField( max_length=100, blank=True)
    steering_side = models.CharField( max_length=100, blank=True)
    color = models.CharField( max_length=100, blank=True)
    equipment = models.CharField( max_length=200, blank=True)
    view_place = models.CharField( max_length=100, blank=True)
    engine_volume = models.FloatField( blank=True, null= True)

    
       
