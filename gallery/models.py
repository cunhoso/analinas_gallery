# models.py
from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='artistas/')
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class ObraDeArte(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='obras/')
    descricao = models.TextField()

    def __str__(self):
        return self.titulo