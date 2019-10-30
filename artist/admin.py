from django.contrib import admin

# importando modelos que serao usados no registro
from .models import Band, Album, Song

admin.site.register(Band) # Permissao pro superusuario registrar banda
admin.site.register(Album) # Album
admin.site.register(Song) # Musica