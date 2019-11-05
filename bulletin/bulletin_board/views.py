import requests

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


from .models import *
from .utils import *
from .forms import CarForm

from django.db.models import Q


def cars_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        cars = Car.objects.filter(Q(car_brand__icontains=search_query) | Q(car_model__icontains=search_query) | Q(year_of_manufacture__icontains=search_query))
    else:
        cars = Car.objects.all()
    
    paginator = Paginator(cars, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context={
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }


    return render(request,'bulletin_board/index.html', context=context)


class CarDetail(ObjectDetailMixin, View):
    model = Car
    template = 'bulletin_board/car_detail.html'




class CarCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    login_url = '/user/login/'
    model_form = CarForm
    template = 'bulletin_board/car_create_form.html'
    
    

class CarUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    login_url = '/user/login/'
    model = Car
    model_form = CarForm
    template = 'bulletin_board/car_update_form.html'
    

class CarDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    login_url = '/user/login/'
    model = Car
    template = 'bulletin_board/car_delete_form.html'
    redirect_url = 'cars_list_url'
    


