from django import forms
from .models import Home, Basic, ContactUs, FAQs

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ('title', 'title_image', 'upcoming_event')

class BasicForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = ('title', 'description')

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('phone_number', 'email')

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQs
        fields = ('question', 'answer')