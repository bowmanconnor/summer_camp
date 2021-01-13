from django.shortcuts import render, redirect, get_object_or_404
from .models import Camp, Camper, Coach
from .forms import NewCampForm, NewCamperForm
from django.utils import timezone
from django.views.generic import UpdateView, DetailView, DeleteView
from django.forms import formset_factory
from django.views import View
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    camps = Camp.objects.all()
    campers = Camper.objects.all()
    return render(request, "home.html", {'camps' : camps, 'campers' : campers})

def new_camp(request):
    if request.method == 'POST':
        form = NewCampForm(request.POST)
        if form.is_valid():
            camp = form.save(commit=False)
            camp.save()
            return redirect('home')
    else:
        form = NewCampForm()
    return render(request, 'core/new_camp.html', {'form': form})

class CampDetailView(DetailView):
    model = Camp
    template_name = 'core/view_camp.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'camp'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context["campers"] = Camper.objects.filter(camp_id=context['object'].id)
        context["num_campers"] = context["campers"].count()
        context['now'] = timezone.now()
        return context

# @login_required
def new_camper(request, pk):
    if request.method == 'POST':
        camper_form_set = formset_factory(NewCamperForm, min_num=1, extra=0)
        form_set = camper_form_set(request.POST)
        if form_set.is_valid():
            for form in form_set:
                camper = form.save(commit=False)
                camper.camp = get_object_or_404(Camp, pk=pk)
                if not (camper.name == '' and camper.age == None and camper.group == ''):
                    camper.save()
            return redirect('home')
    else:
        form_set = formset_factory(NewCamperForm, min_num=1, extra=0)
    return render(request, 'core/new_camper.html', {'form_set': form_set})

class CamperDetailView(DetailView):
    model = Camper
    template_name = 'core/view_camper.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'camper'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context