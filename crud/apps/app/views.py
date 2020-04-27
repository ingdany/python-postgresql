from django.shortcuts import render, redirect
from .models import *
from .forms import PetForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'index.html')

class CreatePet(CreateView):
    model  = Pet
    form_class = PetForm
    template_name = 'app/create_pet.html'
    success_url = reverse_lazy('index')

class ShowPet(ListView):
    model = Pet
    template_name = 'app/show_pet.html'

class UpdatePet(UpdateView):
    model  = Pet
    form_class = PetForm
    template_name = 'app/create_pet.html'
    success_url = reverse_lazy('index')

class DeletePet(DeleteView):
    model  = Pet
    form_class = PetForm
    template_name = 'app/delete_pet.html'
    success_url = reverse_lazy('index')

def createPet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PetForm()
    return render(request, 'app/create_pet.html',{'form':form})

def showPet(request):
    myPet = Pet.objects.all()
    context = {'pet': myPet}
    return render(request, 'app/show_pet.html', context)

def updatePet(request, id):
    pet = Pet.objects.get(id = id)
    if request.method == 'GET':
        form = PetForm(instance = pet)
    else:
        form = PetForm(request.POST, instance = pet)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'app/create_pet.html', {'form': form})

def deletePet(request, id):
    pet = Pet.objects.get(id = id)
    if request.method == 'POST':
        pet.delete()
        return redirect('index')
    return render(request,'app/delete_pet.html',{'pet':pet})