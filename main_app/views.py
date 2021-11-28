from django.shortcuts import render
from .models import List, Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def lists(request):
  lists = List.objects.all()#.filter(user=request.user)
  return render(request, 'lists.html', { 'lists': lists })

def lists_detail(request, list_id):
  list = List.objects.get(id=list_id)
  return render(request, 'lists/detail.html', { 'list': list })

# def list(request, list_id):
#   items = Item.objects.all()#.filter(list=request.list)
#   return render(request, 'list/index.html', { 'items': items})

class ListCreate(CreateView):
  model = List
  fields = '__all__'
  success_url = '/lists/'

class ListUpdate(UpdateView):
  model = List
  fields = '__all__'

class ListDelete(DeleteView):
  model = List
  success_url = '/lists/'