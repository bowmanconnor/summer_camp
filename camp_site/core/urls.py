from django.urls import include, path
import core.views as views

urlpatterns = [
    path('', views.home, name="home"),
    path('camp/new/', views.new_camp, name='new_camp'),
    path('camp/<int:pk>/view/', views.CampDetailView.as_view(), name='view_camp'),
    path('camper/new/<int:pk>/', views.new_camper, name='new_camper'),
    path('camper/<int:pk>/view/', views.CamperDetailView.as_view(), name='view_camper'),


]

    
