from django.contrib import admin
from .models import Artista, ObraDeArte

# Registro dos modelos no painel de administração
admin.site.register(Artista)
admin.site.register(ObraDeArte)
