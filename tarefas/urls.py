from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.add, name='adicionar'),
    path('tarefa/<int:id>/', views.tarefa, name='individual'),
    path('remover/<int:id>/', views.remove, name='remover'),
    path('editar/<int:id>/', views.edit, name='editar'),
    path('buscar/', views.search, name='buscar'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]