from django.forms import ModelForm
from .models import Grocery

class GroceryForm(ModelForm):
  class Meta:
    model = Grocery
    fields = ['date', 'item']