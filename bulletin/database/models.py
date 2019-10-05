from django.db import models

class Car(models.Model):
    car_title = models.CharField( max_length= 100)
    pub_date = models.DateTimeField()
    price = models.FloatField()
    seller = models.CharField( max_length= 100 )
    phone = models.CharField( max_length= 30 )
    car_description = models.TextField()
    car_specs = models.TextField()



