from django.shortcuts import render, redirect
from .models import List, Grocery
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GroceryForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

@login_required
def lists_index(request):
  lists = List.objects.all()#.filter(user=request.user)
  return render(request, 'lists/index.html', { 'lists': lists })

@login_required
def lists_detail(request, list_id):
  list = List.objects.get(id=list_id)
  grocery_form = GroceryForm()
  return render(request, 'lists/detail.html', { 'list': list, 'grocery_form': grocery_form })

@login_required
def add_grocery(request, list_id):
  form = GroceryForm(request.POST)
  # validate the form
  if form.is_valid():
    new_grocery = form.save(commit=False)
    new_grocery.list_id = list_id
    new_grocery.save()
  return redirect('lists_detail', list_id=list_id)

class ListCreate(LoginRequiredMixin, CreateView):
  model = List
  fields = '__all__'
  success_url = '/lists/'
  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)

class ListUpdate(LoginRequiredMixin, UpdateView):
  model = List
  fields = '__all__'
  success_url = '/lists/'

class ListDelete(LoginRequiredMixin, DeleteView):
  model = List
  success_url = '/lists/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('lists_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

  