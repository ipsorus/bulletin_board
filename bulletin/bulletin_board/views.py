from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic import View
from .utils import ObjectDetailMixin

from .models import *
# Create your views here.

def posts_list(request):
    cars = Car.objects.all()
    return render(request,'bulletin_board/index.html', context={'cars': cars})


class PostDetail(ObjectDetailMixin, View):
    model = Car
    template = 'bulletin_board/post_detail.html'
