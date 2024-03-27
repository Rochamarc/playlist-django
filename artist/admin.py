from django.contrib import admin

from .models import Band, Album, Song

# Permision to admin to register 
admin.site.register(Band) 
admin.site.register(Album) 
admin.site.register(Song) 