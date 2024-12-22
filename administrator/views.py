from django.urls import path
from . import views
from . import urls  # Potential circular import


from django.shortcuts import render

def products(request):
    return render(request, 'products.html')
