from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homePage, name= 'homePage' ),
    path('create', views.createAnimal, name= 'createAnimal'),
    path('read', views.readAnimals, name= 'readAnimals')
]