from django.db import models
from django.urls import reverse
from datetime import date



# Create your models here.
class List(models.Model):
  name = models.CharField(max_length=100)
  # user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('lists_form', kwargs={'list_id': self.id})

class Grocery(models.Model):
  item = models.CharField(max_length=100)
  date = models.DateField('List Date')

  list = models.ForeignKey(List, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.item} on {self.date}"
  # def __str__(self):
  #   return self.name

  # def get_absolute_url(self):
  #   return reverse('items_detail', kwargs={'item_id': self.id})