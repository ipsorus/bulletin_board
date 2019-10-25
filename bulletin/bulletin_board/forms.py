from django import forms
from .models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_title', 'price', 'seller', 'phone', 'car_description', 'avito_item', 'car_brand',
        'car_model', 'car_generation', 'modif', 'year_of_manufacture', 'car_mileage', 'condition', 'owners',
        'vin_number', 'type_chassis', 'doors', 'engine_type', 'transmission', 'drive', 'steering_side', 'color',
        'equipment', 'view_place', 'engine_volume']

        widgets = {
            'car_title':forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.TextInput(attrs={'class': 'form-control'}),
            'seller':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'car_description':forms.TextInput(attrs={'class': 'form-control'}),
            'avito_item':forms.TextInput(attrs={'class': 'form-control'}),
            'car_brand':forms.TextInput(attrs={'class': 'form-control'}),
            'car_model':forms.TextInput(attrs={'class': 'form-control'}),
            'car_generation':forms.TextInput(attrs={'class': 'form-control'}),
            'modif':forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_manufacture':forms.TextInput(attrs={'class': 'form-control'}),
            'car_mileage':forms.TextInput(attrs={'class': 'form-control'}),
            'condition':forms.TextInput(attrs={'class': 'form-control'}),
            'owners':forms.TextInput(attrs={'class': 'form-control'}),
            'vin_number':forms.TextInput(attrs={'class': 'form-control'}),
            'type_chassis':forms.TextInput(attrs={'class': 'form-control'}),
            'doors':forms.TextInput(attrs={'class': 'form-control'}),
            'engine_type':forms.TextInput(attrs={'class': 'form-control'}),
            'transmission':forms.TextInput(attrs={'class': 'form-control'}),
            'drive':forms.TextInput(attrs={'class': 'form-control'}),
            'steering_side':forms.TextInput(attrs={'class': 'form-control'}),
            'color':forms.TextInput(attrs={'class': 'form-control'}),
            'equipment':forms.TextInput(attrs={'class': 'form-control'}),
            'view_place':forms.TextInput(attrs={'class': 'form-control'}),
            'engine_volume':forms.TextInput(attrs={'class': 'form-control'})
                    }