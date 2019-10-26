from django.urls import path
from django.contrib.auth import views as auth_views


from user import views
from bulletin_board import urls

app_name = 'user'
urlpatterns = [
    path('register/', views.RegisterView.as_view(),name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]