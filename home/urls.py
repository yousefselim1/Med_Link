
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from signup import views as signup_views 
from login import views as login_views 
from cart import views as cart_views


    
urlpatterns = [
    path('', views.loginaction, name='login'),  # This is the login page as the default
    path('home/', views.index, name='home'),
    path("logout/", LogoutView.as_view(), name="logout"),      # Home page
    path('some-path/', views.index_2, name='index_2'),
    path('login/', login_views.loginaction, name='loginaction'),
    path('', views.index, name='index'),
     path('signup/', signup_views.signup_action, name='signupaction'),

]
