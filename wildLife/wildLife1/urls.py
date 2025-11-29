from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homePage, name= 'homePage' ),
    path('create', views.createAnimal, name= 'createAnimal'),
    path('read', views.readAnimals, name= 'readAnimals'),
    path('readOne/<str:pk>/', views.readOneAnimal, name='readOneAnimal'),
    path('update/<str:pk>/', views.updateAnimal, name='updateAnimal'),
    path('delete/<str:pk>/', views.deleteAnimal, name='deleteAnimal')
]