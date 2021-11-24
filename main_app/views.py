from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class List:  # Note that parens are optional if not inheriting from another class
  def __init__(self, userId, name, createdAt ):
    self.name = name
    self.userId = userId
    self.createAt = createdAt

class Item:  # Note that parens are optional if not inheriting from another class
  def __init__(self, listId, name ):
    self.name = name
    self.listId = listId

listsArray = [
  List('1', 'List 1', ''),
  List('1', 'List 2', ''),
  List('2', 'List 3', ''),
  List('2', 'List 4', '')
]

items = [
  Item('1', 'Beer'),
  Item('1', 'Wine')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
def lists(request):
  return render(request, 'lists.html', { 'lists': listsArray })
def list(request, list_id):
  return render(request, 'list/index.html', { 'items': items})
