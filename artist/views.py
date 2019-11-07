from django.shortcuts import render

# importing my models
from .models import Band, Album, Song
# import helpful libs
from .lib import list_check, artist_check, return_album, take_top_bands, take_top_albums

def index(request):
    song_list = Song.objects.all()
    band_list = Band.objects.all()

    short_song_list = list_check(song_list,5) # return a list with 5 random songs

    artist_rate = artist_check(band_list)
    band_list = list_check(artist_rate,4) # return a list with 4 random rated bands

    context = { 'song_list': short_song_list, 'band_list': band_list }
    return render(request,'artist/index.html', context) # busca pelo template na pasta template

# Artist index
def bands_index(request):
    band_list = Band.objects.all()
    context = { 'band_list': band_list }
    return render(request, 'artist/bands.html', context)

# Show details of the artist
def band_detail(request, pk):
    band_detail = Band.objects.filter(id=pk)
    song_band_detail = Song.objects.filter(song_artist = band_detail[0])
    album_band_detail = Album.objects.filter(album_band = band_detail[0])
    context = { 
        'pk': pk, 
        'band_detail': band_detail, 
        'song_band_detail': song_band_detail, 
        'album_band_detail': album_band_detail 
    }
    return render(request, 'artist/band_detail.html', context)

# Page of the most rated album and bands
def top_index(request):
    top_bands = list(Band.objects.all())
    top_albums = list(Album.objects.all())
    

    top_bands.sort(key=take_top_bands, reverse=True) # sort by band votes
    top_albums.sort(key=take_top_albums, reverse=True) # sort by album votes

    context = {
        'top_bands': top_bands,
        'top_albums': top_albums
    }

    return render(request, 'artist/top.html', context)