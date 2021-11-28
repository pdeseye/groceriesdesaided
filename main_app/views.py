from django.shortcuts import render, redirect
from .models import List, Grocery
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GroceryForm

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def lists_index(request):
  lists = List.objects.all()#.filter(user=request.user)
  return render(request, 'lists/index.html', { 'lists': lists })

def lists_detail(request, list_id):
  list = List.objects.get(id=list_id)
  grocery_form = GroceryForm()
  return render(request, 'lists/detail.html', { 'list': list, 'grocery_form': grocery_form })

def add_grocery(request, list_id):
  form = GroceryForm(request.POST)
  # validate the form
  if form.is_valid():
    new_grocery = form.save(commit=False)
    new_grocery.list_id = list_id
    new_grocery.save()
  return redirect('lists_detail', list_id=list_id)

class ListCreate(CreateView):
  model = List
  fields = '__all__'
  success_url = '/lists/'

class ListUpdate(UpdateView):
  model = List
  fields = '__all__'
  success_url = '/lists/'

class ListDelete(DeleteView):
  model = List
  success_url = '/lists/'