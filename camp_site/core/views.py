from django.shortcuts import render, redirect, get_object_or_404
from .models import Camp, Camper, Coach
from .forms import NewCampForm, NewCamperForm
from django.utils import timezone
from django.views.generic import UpdateView, DetailView, DeleteView


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

# @method_decorator(staff_member_required(login_url='home') , name='dispatch')




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

def new_camper(request):
    if request.method == 'POST':
        form = NewCamperForm(request.POST)
        if form.is_valid():
            camper = form.save(commit=False)
            camper.save()
            camper.camp.number_campers += 1
            return redirect('home')
    else:
        form = NewCamperForm()
    return render(request, 'core/new_camper.html', {'form': form})

# @method_decorator(staff_member_required(login_url='home') , name='dispatch')

class CamperDetailView(DetailView):
    model = Camper
    template_name = 'core/view_camper.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'camper'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context