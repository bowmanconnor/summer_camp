from django.urls import include, path
import authentication.views as views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register, name="register"),
    path('edit/', views.UserUpdateView.as_view(), name='edit_account'),
]