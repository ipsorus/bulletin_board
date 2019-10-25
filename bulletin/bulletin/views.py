from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_main_page(request):
    return redirect('cars_list_url',permanent=True)