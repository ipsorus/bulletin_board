from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:id>/', PostDetail.as_view(), name="post_detail_url")

]