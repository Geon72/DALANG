from django.urls import path
from . import views

urlpatterns = [
    path('exchange_rate_view/', views.exchange_rate_view, name='exchange_rate_view'),
    path('exchange_rate_chart_view/', views.exchange_rate_chart_view, name='exchange_rate_chart_view'),
]