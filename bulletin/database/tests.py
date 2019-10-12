import datetime

from django.utils import timezone
from django.test import TestCase
from model_mommy import mommy

from .models import Car

class CarModelTests(TestCase):

    def test_wrong_date_type(self):
       
        test_car = mommy.make(Car)
        self.assertTrue(isinstance(test_car, Car))
        
        
        

