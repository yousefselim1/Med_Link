"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path , include
from signup.views import signupaction
from login.views import loginaction
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from home import views

print("Loading URLs...")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signupaction),
    path('login/',loginaction),
    # path('', views.index, name='home'),
    path('search/', include('search.urls')),
    path('accounts/', include('allauth.urls')),
    path("/", include("users.urls")),
    path('', include('home.urls')),
    path('payment/', include('payment.urls')),
    path('profile/', include('personal.urls')),
    path('notification/', include('notification.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
    path('products/', include('products.urls')),
    path('ColdAndFlu/', include('ColdAndFlu.urls')),
    path('PainRelief/', include('PainRelief.urls')),
    path('adminstrator/', include('administrator.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]




