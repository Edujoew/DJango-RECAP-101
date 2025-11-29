from django.shortcuts import render , redirect
from django.http import    HttpResponse
from .models import Animals
from .forms import AnimalsForm
# Create your views here.

def homePage(request):
    return render (request, 'wildlife1/home.html')

def createAnimal(request):
    form = AnimalsForm()

    if request.method == "POST": 
        form = AnimalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("homePage")

    context = {"form": form}   
    return render (request , 'wildLife1/forms.html',context)     

def readAnimals(request):
    animalss=Animals.objects.all()
    context={"animalss":animalss}
    return render (request, 'wildlife1/Animals.html',context)