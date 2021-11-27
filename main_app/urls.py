from django.urls import path
from . import views

urlpatterns = [

  path('', views.home, name='home'),
  path('lists/', views.lists, name='lists'),
  path('lists/<int:list_id>/', views.list, name='list'),
  path('lists/create/', views.ListCreate.as_view(), name='lists_create'),
  path('lists/<int:pk>/update/', views.ListUpdate.as_view(), name='lists_update'),
path('lists/<int:pk>/delete/', views.ListDelete.as_view(), name='lists_delete'),
]

