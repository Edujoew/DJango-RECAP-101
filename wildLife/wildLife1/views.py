from django.shortcuts import render , redirect
from django.http import    HttpResponse
from .models import Animals
from .forms import AnimalsForm
# Create your views here.

def homePage(request):
    return render (request, 'wildlife1/home.html')

# Create animals
def createAnimal(request):
    form = AnimalsForm()

    if request.method == "POST": 
        form = AnimalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("readAnimals")

    context = {"form": form}   
    return render (request , 'wildLife1/forms.html',context)     

# Read animals
def readAnimals(request):
    animalss=Animals.objects.all()
    context={"animalss":animalss}
    return render (request, 'wildlife1/Animals.html',context)

# Read one animal 
def readOneAnimal(request, pk):
    animals=Animals.objects.get(id=pk)
    context={'animals':animals}
    return render(request, 'wildLife1/Animal.html', context)

# Update animal
def updateAnimal(request, pk):
    animals = Animals.objects.get(id=pk)
    form = AnimalsForm(instance = animals)

    if request.method == "POST":
        form = AnimalsForm(request.POST, instance = animals)
        if form.is_valid():
            form.save()
            return redirect("readAnimals")

    context = {"form": form}
    return render(request, "wildLife1/forms.html", context)

# Delete animal
def deleteAnimal(request, pk):
    animals = Animals.objects.get(id=pk)

    if request.method == "POST":
        animals.delete()
        return redirect("readAnimals")

    context = {"animals": animals}
    return render(request, "wildLife1/delete.html", context)