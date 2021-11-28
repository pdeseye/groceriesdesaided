from django.urls import path
from . import views

urlpatterns = [

  path('', views.home, name='home'),
  path('lists/', views.lists_index, name='lists_index'),
  path('lists/<int:list_id>/', views.lists_detail, name='lists_detail'),
  path('lists/create/', views.ListCreate.as_view(), name='lists_create'),
  path('lists/<int:pk>/update/', views.ListUpdate.as_view(), name='lists_update'),
  path('lists/<int:pk>/delete/', views.ListDelete.as_view(), name='lists_delete'),
  path('lists/<int:list_id>/add_grocery/', views.add_grocery, name='add_grocery'),
]

