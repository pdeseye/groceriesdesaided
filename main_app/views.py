from django.shortcuts import render
from .models import List, Item

# Add the following import
from django.http import HttpResponse



items = [
  Item('1', 'Beer'),
  Item('1', 'Wine')
]

# Define the home view
def home(request):
  return render(request, 'home.html')
def lists(request):
  lists = List.objects.all()#.filter(user=request.user)

  return render(request, 'lists.html', { 'lists': lists })
def list(request, list_id):
  return render(request, 'list/index.html', { 'items': items})
