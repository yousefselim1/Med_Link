from django.urls import path
from . import views

urlpatterns = [
    path('cold-and-flu/', views.cold_and_flu, name='cold_and_flu')
]