from django.urls import include, path
import editable_pages.views as views


urlpatterns = [
    path('', views.home, name="home"),
    path('edit/homepage/<int:pk>/', views.HomeUpdateView.as_view(), name='edit_home'),
]