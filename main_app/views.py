from django.shortcuts import render

finches = [
  {'name': 'Scary', 'breed': 'House', 'description': 'feathery little demon', 'age': 3},
  {'name': 'Ugg', 'breed': 'Purple', 'description': 'weird hair', 'age': 2},
  {'name': 'Ewy', 'breed': 'Dessert', 'description': 'very dull color', 'age': 5},
  {'name': 'Chicky', 'breed': 'Atlantic', 'description': 'yellow like a chick', 'age': 0},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })