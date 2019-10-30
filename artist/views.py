from django.shortcuts import render

# importing my models
from .models import Band, Album, Song

def index(request):
    song_list = Song.objects.all()
    band_list = Band.objects.all()

    context = { 'song_list': song_list, 'band_list': band_list }
    return render(request,'artist/index.html', context) # busca pelo template na pasta template

# Artist index
def show_bands(request):
    band_list = Band.objects.all()
    context = { 'band_list': band_list }
    return render(request, 'artist/bands.html', context)

# Show details of the artist
def band_detail(request, pk):
    band_detail = Band.objects.filter(id=pk)
    song_band_detail = Song.objects.filter(song_artist = band_detail.band_name)
    album_band_detail = Album.objects.filter(album_artist = band_detail.band_name)
    context = { 
        'pk': pk, 
        'band_detail': band_detail, 
        'song_band_detail': song_band_detail, 
        'album_band_detail': album_band_detail 
    }
    return render(request, 'artist/band_detail.html', context)

