
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect


    
urlpatterns = [
    path('', views.loginaction, name='login'),  # This is the login page as the default
    path('home/', views.index, name='home'),
    path("logout/", LogoutView.as_view(), name="logout"),      # Home page

]
