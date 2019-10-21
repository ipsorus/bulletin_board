from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:id>/', post_detail, name="post_detail_url")

]