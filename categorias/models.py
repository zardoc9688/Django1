from django.db import models

# Create your models here.
class Categorias(models.Model):
    name  = models.CharField(max_length=100)