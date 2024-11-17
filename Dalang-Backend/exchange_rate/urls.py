from django.urls import path
from . import views

urlpatterns = [
    path('exchange_rate/', views.exchange_rate, name='exchange_rate'),
]