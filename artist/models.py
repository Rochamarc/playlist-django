from django.db import models


class Band(models.Model):
    band_name = models.Charfield(max_length = 100)
    band_bio = models.TextField(default = "Band's biography")
    band_genre = models.Charfield(max_length = 50)


class Album(models.Model):
    album_name = models.CharField(max_length = 100)
    album_length = models.Charfield(max_length = 6)
    album_year = models.DateField()
    album_band = models.ForeignKey(Band, on_delete=models.CASCADE)

class Song(models.Model):
    song_name = models.CharField(max_length = 50)
    song_number = models.IntegerField()
    song_artist = models.ForeignKey(Band, on_delete=models.CASCADE)
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)