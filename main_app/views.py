from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# finches = [
#   {'name': 'Scary', 'breed': 'House', 'description': 'feathery little demon', 'age': 3},
#   {'name': 'Ugg', 'breed': 'Purple', 'description': 'weird hair', 'age': 2},
#   {'name': 'Ewy', 'breed': 'Dessert', 'description': 'very dull color', 'age': 5},
#   {'name': 'Chicky', 'breed': 'Atlantic', 'description': 'yellow like a chick', 'age': 0},
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/{id}'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'