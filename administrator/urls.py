from django.urls import path
from . import views

urlpatterns = [
    path('administrator', views.products, name='administrator'),
]
