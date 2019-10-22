from django.shortcuts import render

from .models import Car
# Create your views here.

def posts_list(request):
    posts = Car.objects.all()
    return render(request,'bulletin_board/index.html', context={'posts': posts})


def post_detail(request, id):
    post = Car.objects.get(id__iexact=id)
    return render(request, 'bulletin_board/post_detail.html', context={'post':post})
