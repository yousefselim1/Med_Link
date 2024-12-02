from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_drugs, name='search_drugs'),  # Search page
]
