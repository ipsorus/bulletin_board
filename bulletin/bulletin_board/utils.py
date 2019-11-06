from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self,request,id):
        obj = get_object_or_404(self.model, id__iexact=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj, 'detail': True})

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST, request.FILES)
        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.seller = request.user
            new_obj = bound_form.save()
            for f in request.FILES.getlist('all_images'):
                data = f.read() #Если файл целиком умещается в памяти
                photo = Photo(car=new_obj)
                photo.image_data_link.save(f.name, ContentFile(data))
                photo.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        bound_form = self.model_form(request.POST, request.FILES, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            for f in request.FILES.getlist('all_images'):
                data = f.read() #Если файл целиком умещается в памяти
                photo = Photo(car=new_obj)
                photo.image_data_link.save(f.name, ContentFile(data))
                photo.save()
            return redirect(new_obj)
        return render(redirect, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        return render(request, self.template, context={self.model.__name__.lower():obj})

    def post(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        obj.delete()
        return redirect(reverse(self.redirect_url))

