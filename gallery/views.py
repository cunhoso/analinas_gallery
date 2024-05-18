from django.shortcuts import render
from .models import Artista

def pagina_inicial(request):
    artistas = Artista.objects.all()
    return render(request, 'galeria/pagina_inicial.html', {'artistas': artistas})

def pagina_artista(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    obras = artista.obradearte_set.all()
    return render(request, 'galeria/pagina_artista.html', {'artista': artista, 'obras': obras})
