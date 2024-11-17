from django.urls import path
from . import views

urlpatterns = [
    path('kakaomap/', views.kakaomap, name='kakaomap'),
]