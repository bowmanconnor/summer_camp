from django import forms
from .models import Event, Coach, Gymnast
from django.contrib.auth.models import User

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'start_date', 'end_date', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code')

class NewGymnastForm(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = ('name', 'age', 'group')

class NewCoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('name', 'bio', 'pic')