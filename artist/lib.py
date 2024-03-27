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
    
def artist_check(query_set: list) -> list:
    """Check if the artist has more than 10 votes
    """
    
    return [ i.votes >= 10 for i in query_set ]

def return_album(model):
    """Filter and album by a model Band
    """

    return Album.objects.filter(band = model.name)

def take_top_bands(object):
    return object.votes

def take_top_albums(object):
    return object.votes
