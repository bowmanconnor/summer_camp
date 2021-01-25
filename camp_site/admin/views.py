from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic import UpdateView, DetailView, DeleteView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from core.models import Event, Gymnast
from editable_pages.models import Home, ContactUs, FAQs, Basic


# Create your views here.

@staff_member_required(login_url='home')
def dashboard(request):
    return render(request, "admin/dashboard.html")

def events(request):
    context = {}
    context['events'] = Event.objects.all()

    return render(request, "admin/events.html", context)

class HomeUpdateView(UpdateView):
    model = Home
    fields = ('title', 'title_image', 'upcoming_event')

    template_name = 'admin/edit_home.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'home'

    def form_valid(self, form):
        home = form.save(commit=False)
        home.save()
        return redirect('dashboard')


class EventDetailView(DetailView):
    model = Event
    template_name = 'admin/view_event.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context["gymnasts"] = Gymnast.objects.filter(event_id=context['object'].id)
        context["num_gymnasts"] = context["gymnasts"].count()
        context['now'] = timezone.now()
        return context 

class EventUpdateView(UpdateView):
    model = Event
    fields = ('name', 'description', 'start_date', 'end_date', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code', 'is_open')

    template_name = 'admin/edit_event.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'event'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return redirect('view_event_admin', event.pk)