from .models import Album
import random

def list_check(query_set: list, length: int) -> list:
    """Makes a check on the query_set getting random values from it

    Parameters
    ----------
    query_set : list
        A list containing the data to be add on the returns
    length : int
        Length of the return list
    
    Returns
    -------
        A list with length of the length parameters and random values from the enter query_set
    """

    query_set = list(query_set)
    random.shuffle(query_set)

    try:
        return [ query_set.pop() for _ in range(length) ]
    except:
        return query_set
    
def most_rated_artists(artist_set: list, rate_value: int=10) -> list:
    """Filter artists by rate

    Parameters
    ----------
    artist_set : queryset
        Band queryset
    rate_value: int
        A rate value for the Band votes
    
    Returns
    -------
        A list of Bands filtered by number of votes 
    """
    
    return [ artist.votes >= rate_value for artist in artist_set ]

def return_album(model):
    """Filter and album by a model Band"""

    return Album.objects.filter(band = model.name)

def take_top(object):
    """Return an object values"""
    return object.values