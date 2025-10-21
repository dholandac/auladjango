from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.add, name='adicionar'),
    path('remover/', views.remove, name='remover'),
    path('editar/', views.edit, name='editar'),
    path('buscar/', views.search, name='buscar')
]