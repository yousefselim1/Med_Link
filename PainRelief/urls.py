from django.urls import path
from . import views

urlpatterns = [
    path('pain-relief/', views.pain_relief, name='pain_relief')
]