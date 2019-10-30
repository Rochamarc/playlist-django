from django.db import models

from django.utils import timezone

class Band(models.Model):
    band_name = models.CharField(max_length = 100)
    band_bio = models.TextField(default = "Artist Biography")
    band_genre = models.CharField(max_length = 50)
    band_origin = models.CharField(max_length = 50)
    band_photo = models.TextField(default = "Artist Image")
    band_votes = models.IntegerField(default = 1)
    def __str__(self):
        return self.band_name


class Album(models.Model):
    album_name = models.CharField(max_length = 100)
    album_length = models.CharField(max_length = 7)
    album_year = models.DateField()
    album_band = models.ForeignKey(Band, on_delete=models.CASCADE)
    album_image = models.TextField(default = "Album Image")
    album_votes = models.IntegerField(default = 1)
    def __str__ (self):
        return self.album_name 

class Song(models.Model):
    song_name = models.CharField(max_length = 50)
    song_number = models.IntegerField()
    song_length = models.CharField(max_length = 7)
    song_artist = models.ForeignKey(Band, on_delete=models.CASCADE)
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.song_name