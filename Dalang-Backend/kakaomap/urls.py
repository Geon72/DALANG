from django.urls import path
from . import views

urlpatterns = [
    path('', views.kakaomap, name='kakaomap'),
]