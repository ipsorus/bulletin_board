from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name="post_create_url"),
    path('post/<str:id>/', PostDetail.as_view(), name="post_detail_url"),
    path('post/<str:id>/update/', PostUpdate.as_view(), name="post_update_url")

]