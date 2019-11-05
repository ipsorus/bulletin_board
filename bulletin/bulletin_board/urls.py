from django.urls import path
from .views import *


urlpatterns = [
    path('', cars_list, name='cars_list_url'),
    path('car/create/', CarCreate.as_view(), name="car_create_url"),
    path('car/<int:id>/', CarDetail.as_view(), name="car_detail_url"),
    path('car/<int:id>/update/', CarUpdate.as_view(), name="car_update_url"),
    path('car/<int:id>/delete/', CarDelete.as_view(), name="car_delete_url"),
    path('users/', users_list, name='users_list')

]