import requests

from django.db import models
from django.core.files import File
from tempfile import NamedTemporaryFile
from django.utils import timezone

from django.shortcuts import reverse


class Car(models.Model):
   
    car_title = models.CharField(max_length=100, blank=True, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, null= True)
    seller = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    car_description = models.TextField(blank=True)
    avito_item = models.CharField(max_length=100, blank=True)
    car_brand = models.CharField(max_length=100, blank=True, db_index=True)
    car_model = models.CharField(max_length=100, blank=True, db_index=True)
    car_generation = models.CharField(max_length=100, blank=True)
    modif = models.CharField(max_length=100, blank=True)
    year_of_manufacture = models.IntegerField(null=True, db_index=True)
    car_mileage = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True)
    owners = models.IntegerField(blank=True, null=True)
    vin_number = models.CharField(max_length=100, blank=True)
    type_chassis = models.CharField(max_length=100, blank=True)
    doors = models.IntegerField(blank=True, null=True)
    engine_type = models.CharField(max_length=100, blank=True)
    transmission = models.CharField(max_length=100, blank=True)
    drive = models.CharField(max_length=100, blank=True)
    steering_side = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    equipment = models.CharField(max_length=200, blank=True)
    view_place = models.CharField(max_length=100, blank=True)
    engine_volume = models.FloatField(blank=True, null= True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'id': self.id})


    def __str__(self):
        return self.car_title

class Photos(models.Model):

    image_data_link = models.ImageField(upload_to='photos/%Y/%m/%d')
    image_url = models.URLField(blank=True)
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name='resultimage')

    def get_remote_url(self):
        if self.image_url and not self.image_data_link:
            image_temp = NamedTemporaryFile(delete=True)
            image_temp.write(requests.get(self.image_url).content)
            image_temp.flush()
            self.image_data_link.save(f'photo_{self.pk}.jpg', File(image_temp))
        self.save()



