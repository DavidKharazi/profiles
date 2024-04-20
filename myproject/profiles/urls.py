from django.urls import path
from . import views

urlpatterns = [
    path('customer/profile/', views.customer_profile, name='customer_profile'),
    path('performer/profile/', views.performer_profile, name='performer_profile'),
]
