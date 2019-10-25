from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .utils import *
from .forms import CarForm


def cars_list(request):
    cars = Car.objects.all()
    return render(request,'bulletin_board/index.html', context={'cars': cars})


class CarDetail(ObjectDetailMixin, View):
    model = Car
    template = 'bulletin_board/car_detail.html'

class CarCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = CarForm
    template = 'bulletin_board/car_create_form.html'
    raise_exception = True

class CarUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Car
    model_form = CarForm
    template = 'bulletin_board/car_update_form.html'
    raise_exception = True

class CarDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Car
    template = 'bulletin_board/car_delete_form.html'
    redirect_url = 'cars_list_url'
    raise_exception = True


