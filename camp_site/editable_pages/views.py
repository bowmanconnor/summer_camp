from django.shortcuts import render, redirect, get_object_or_404
from .models import Home, ContactUs, FAQs, Basic
from core.models import Event
from .forms import HomeForm, ContactUsForm, FAQForm, BasicForm
from django.utils import timezone
from django.views.generic import UpdateView, DetailView, DeleteView
from django.views import View
# Create your views here.

def home(request):
    context = {}
    context['homeData'] = Home.objects.all()[0]
    context['events'] = Event.objects.filter(is_open=True)
    return render(request, 'editable_pages/home.html', context)

class HomeUpdateView(UpdateView):
    model = Home
    fields = ('title', 'title_image', 'upcoming_event')

    template_name = 'editable_pages/edit_home.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'home'

    def form_valid(self, form):
        home = form.save(commit=False)
        home.save()
        return redirect('home')


