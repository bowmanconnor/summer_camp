from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Gymnast, Coach
from .forms import NewEventForm, NewGymnastForm, NewCoachForm
from django.utils import timezone
from django.views.generic import UpdateView, DetailView, DeleteView
from django.forms import formset_factory
from django.views import View
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    context = {}
    context['events'] = Event.objects.all()
    context['gymnasts'] = Gymnast.objects.all()
    context['coaches'] = Coach.objects.all()
    return render(request, "home.html", context)

#--------------------------------------------------------------------------------------------------------

def new_event(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('home')
    else:
        form = NewEventForm()
    return render(request, 'core/new_event.html', {'form': form})

class EventDetailView(DetailView):
    model = Event
    template_name = 'core/view_event.html'
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
    fields = ('name', 'description', 'date', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code', 'is_open')

    template_name = 'core/edit_event.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'event'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return redirect('home')

#--------------------------------------------------------------------------------------------------------

# @login_required
def new_gymnast(request, pk):
    if request.method == 'POST':
        gymnast_form_set = formset_factory(NewGymnastForm, min_num=1, extra=0)
        form_set = gymnast_form_set(request.POST)
        if form_set.is_valid():
            for form in form_set:
                gymnast = form.save(commit=False)
                gymnast.event = get_object_or_404(Event, pk=pk)
                if not (gymnast.name == '' and gymnast.age == None and gymnast.group == ''):
                    gymnast.save()
            return redirect('home')
    else:
        form_set = formset_factory(NewGymnastForm, min_num=1, extra=0)
    return render(request, 'core/new_gymnast.html', {'form_set': form_set})

class GymnastDetailView(DetailView):
    model = Gymnast
    template_name = 'core/view_gymnast.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'gymnast'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class GymnastUpdateView(UpdateView):
    model = Gymnast
    fields = ('name', 'age', 'group', 'event')

    template_name = 'core/edit_gymnast.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'gymnast'

    def form_valid(self, form):
        gymnast = form.save(commit=False)
        gymnast.save()
        return redirect('home')

#--------------------------------------------------------------------------------------------------------

def new_coach(request):
    if request.method == 'POST':
        form = NewCoachForm(request.POST)
        if form.is_valid():
            coach = form.save(commit=False)
            coach.save()
            return redirect('home')
    else:
        form = NewCoachForm()
    return render(request, 'core/new_coach.html', {'form': form})

class CoachDetailView(DetailView):
    model = Event
    template_name = 'core/view_coach.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'coach'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CoachUpdateView(UpdateView):
    model = Event
    fields = ('name', 'bio', 'pic')

    template_name = 'core/edit_coach.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'event'

    def form_valid(self, form):
        coach = form.save(commit=False)
        coach.save()
        return redirect('home')
