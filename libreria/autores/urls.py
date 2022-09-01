from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('autores/', views.listarAutores, name='autores'),
    path('autores/new', views.crear_autor, name='nuevo_autor'),
    path('autores/<id>/', views.autor_view, name='autor_view'),
    path('autores/update/<id>/', views.update_autor, name='autor_actualizar'),
    path('autores/delete/<id>/', views.delete_view, name='autor_eliminar'),
]