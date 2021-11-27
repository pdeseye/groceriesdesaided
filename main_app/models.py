from django.db import models
from django.urls import reverse
from datetime import date



# Create your models here.
class List(models.Model):
  name = models.CharField(max_length=100)
  #user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('list_detail', kwargs={'list_id': self.id})

class Item(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('item_detail', kwargs={'item_id': self.id})