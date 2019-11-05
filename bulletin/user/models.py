from django.db import models
from django.contrib.auth.models import User
from .forms import RegisterForm
from bulletin_board.models import Car

class FavoriteBase(models.Model):
    class Meta:
        abstract = True
 
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete = models.PROTECT)
 
    def __str__(self):
        return self.user.username

class FavoriteCar(FavoriteBase):
    class Meta:
        db_table = "Favorite_car"
 
    obj = models.ForeignKey(Car, verbose_name="Объявление", on_delete = models.PROTECT)
 
   


