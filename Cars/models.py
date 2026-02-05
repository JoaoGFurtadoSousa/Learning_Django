from django.db import models
from Marcas.models import Marca
# Create your models here.

class Cars(models.Model):
    nome = models.CharField(max_length= 50)
    ano = models.IntegerField()
    preco = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.nome