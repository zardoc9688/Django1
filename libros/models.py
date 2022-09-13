from django.db import models

from autores.models import Autor
from categorias.models import Categorias

# Create your models here.
class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    fecha_pub = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now=True)