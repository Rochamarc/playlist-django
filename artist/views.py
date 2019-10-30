from django.shortcuts import render

# importing my models
from .models import Band, Album, Song

def index(request):
    song_list = Song.objects.all()
    band_list = Band.objects.all()
    context = { 'song_list': song_list, 'band_list': band_list }
    # artist/index.html --> arquivo index na pasta de templates no repositorio atual
    # lembre-se isso não é uma rota
    return render(request,'artist/index.html', context)
