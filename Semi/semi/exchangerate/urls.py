from django.urls import path
from . import views

urlpatterns = [
    path('exchangerate/', views.exchangerate, name='exchangerate'),
]