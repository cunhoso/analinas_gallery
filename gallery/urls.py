from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('artista/<int:artista_id>/', views.pagina_artista, name='pagina_artista'),
]
