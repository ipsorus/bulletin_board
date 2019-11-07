import requests

from django.db import models
from django.core.files import File
from tempfile import NamedTemporaryFile
from django.utils import timezone

from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings

from sorl.thumbnail import ImageField


class Car(models.Model):
   
    car_title = models.CharField('Заголовок объявления', max_length=100, blank=True, db_index=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    price = models.IntegerField('Цена', blank=True, null= True)
    seller = models.ForeignKey(User, default=1, on_delete=models.CASCADE, verbose_name = "Продавец")
    phone = models.CharField('Телефон', max_length=30, blank=True)
    car_description = models.TextField('Описание', blank=True)
    avito_item = models.CharField('Авито номер', max_length=100, blank=True)
    car_brand = models.CharField('Марка авто', max_length=100, blank=True, db_index=True)
    car_model = models.CharField('Модель авто', max_length=100, blank=True, db_index=True)
    car_generation = models.CharField('Поколение', max_length=100, blank=True)
    modif = models.CharField('Модификация', max_length=100, blank=True)
    year_of_manufacture = models.IntegerField('Год производства', null=True, db_index=True)
    car_mileage = models.IntegerField('Пробег', blank=True, null=True)
    condition = models.CharField('Состояние', max_length=100, blank=True)
    owners = models.IntegerField('Количество владельцев', blank=True, null=True)
    vin_number = models.CharField('VIN номер', max_length=100, blank=True)
    type_chassis = models.CharField('Кузов', max_length=100, blank=True)
    doors = models.IntegerField('Количество дверей', blank=True, null=True)
    engine_type = models.CharField('Тип двигателя', max_length=100, blank=True)
    transmission = models.CharField('Трансмиссия', max_length=100, blank=True)
    drive = models.CharField('Привод', max_length=100, blank=True)
    steering_side = models.CharField('Руль', max_length=100, blank=True)
    color = models.CharField('Цвет', max_length=100, blank=True)
    equipment = models.CharField('Дополнительное оборудование', max_length=200, blank=True)
    view_place = models.CharField('Место осмотра', max_length=100, blank=True)
    engine_volume = models.FloatField('Объем двигателя', blank=True, null= True)

    class Meta:
        verbose_name = "Автомобили"
        verbose_name_plural = "Автомобили"
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('car_detail_url', kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('car_update_url', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('car_delete_url', kwargs={'id':self.id})


    def __str__(self):
        return self.car_title

class Photo(models.Model):

    image_data_link = ImageField(upload_to='photos/%Y/%m/%d')
    image_url = models.URLField(blank=True)
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name='all_images')

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def get_remote_url(self):
        if self.image_url and not self.image_data_link:
            image_temp = NamedTemporaryFile(delete=True)
            image_temp.write(requests.get(self.image_url).content)
            image_temp.flush()
            self.image_data_link.save(f'photo_{self.pk}.jpg', File(image_temp))
        self.save()



