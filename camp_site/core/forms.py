from django import forms
from .models import Camp, Camper, Coach
from django.contrib.auth.models import User

class NewCampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ('name', 'description', 'date', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code')

class NewCamperForm(forms.ModelForm):
    class Meta:
        model = Camper
        fields = ('name', 'age', 'group')

    
