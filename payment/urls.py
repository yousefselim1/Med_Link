from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('payment/', views.payment_view, name='payment_view'),  # Make sure the view function and the name are correct
]
