from django.urls import include, path
import core.views as views

urlpatterns = [
    path('data/', views.data, name="data"),
    path('event/new/', views.new_event, name='new_event'),
    path('event/<int:pk>/view/', views.EventDetailView.as_view(), name='view_event'),
    path('event/<int:pk>/register', views.register, name='register'),
    path('gymnast/<int:pk>/view/', views.GymnastDetailView.as_view(), name='view_gymnast'),
    path('gymnast/<int:pk>/edit', views.GymnastUpdateView.as_view(), name='edit_gymnast'),
    path('coach/new/', views.new_coach, name='new_coach'),
    path('coach/<int:pk>/view/', views.CoachDetailView.as_view(), name='view_coach'),
    path('coach/<int:pk>/edit', views.CoachUpdateView.as_view(), name='edit_coach'),

]

    
