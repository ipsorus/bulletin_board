import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Car

class CarModelTests(TestCase):

    def test_wrong_date_type(self):
        """
        returns False, if published date has wrong type
        """
        test_car = Car(pub_date = 'получаю какие-то данные' )
        self.assertIs(type(test_car.pub_date) is datetime.datetime, True)
        
        
        

