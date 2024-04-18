from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p1/', views.proyecto1, name='proyecto1'),
    path('p2/', views.proyecto2, name='proyecto2'),
]
