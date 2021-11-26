from django.urls import path
from . import views

urlpatterns = [

  path('', views.home, name='home'),
  path('lists/', views.lists, name='lists'),
  path('lists/<int:list_id>/', views.list, name='list')
]

