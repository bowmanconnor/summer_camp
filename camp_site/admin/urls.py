from django.contrib import admin
from django.urls import include, path
import admin.views as views

urlpatterns = [
    path('django/settings', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events/', views.events, name='events'),
    path('edit/homepage/<int:pk>/', views.HomeUpdateView.as_view(), name='edit_home'),
    path('view/event/<int:pk>/', views.EventDetailView.as_view(), name='view_event_admin'),
    path('event/<int:pk>/edit', views.EventUpdateView.as_view(), name='edit_event'),

]