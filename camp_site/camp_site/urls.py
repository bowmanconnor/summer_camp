"""camp_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import core.views as core_views
import authentication.views as authentication_views
# from authentication.forms import UserLoginForm

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', authentication_views.register, name="register"),
    path('account/edit/', authentication_views.UserUpdateView.as_view(), name='edit_account'),
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('', include('social_django.urls', namespace='social'))

]
