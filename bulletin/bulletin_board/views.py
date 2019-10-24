from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *
from .utils import *
from .forms import PostForm


def posts_list(request):
    cars = Car.objects.all()
    return render(request,'bulletin_board/index.html', context={'cars': cars})


class PostDetail(ObjectDetailMixin, View):
    model = Car
    template = 'bulletin_board/post_detail.html'

class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'bulletin_board/car_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Car
    model_form = PostForm
    template = 'bulletin_board/car_update_form.html'

