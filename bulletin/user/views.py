import requests

from django.shortcuts import render

from django.contrib import auth
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from .models import FavoriteCar


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')

class FavoriteView(View):

    model = None
 
    def add_delete_favorite(self, request, pk):
        user = auth.get_user(request)
        favorite, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        if not created:
            favorite.delete()
 
        return HttpResponseRedirect('/bulletin_board/')


