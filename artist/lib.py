def list_check(enter_list,length):
    from random import choice

    out_list = [] 

    i = 1
    while i <= length:
        i += 1
        append_value = choice(enter_list)
        if append_value in out_list:
            i -= 1
        else:
            out_list.append(append_value)
    
    return out_list 

def artist_check(enter_list):

    out_list = []

    for i in enter_list:
        if i.band_votes >= 10:
            out_list.append(i)
    
    return out_list

def return_album(model):
    from .models import Album

    return Album.objects.filter(album_band = model.band_name)

def take_top_bands(object):
    return object.band_votes

def take_top_albums(object):
    return object.album_votes
