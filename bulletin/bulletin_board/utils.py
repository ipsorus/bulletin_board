from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self,request,id):
        obj = get_object_or_404(self.model, id__iexact=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
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
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(redirect, self.template, context={'form': bound_form, self.model.__name.lower(): obj})

