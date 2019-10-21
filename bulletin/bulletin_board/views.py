from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request,'bulletin_board/index.html')
