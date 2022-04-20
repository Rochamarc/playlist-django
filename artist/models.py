from django.db import models

class Band(models.Model):
    
    name = models.CharField(max_length = 100)
    bio = models.TextField(default = "Artist Biography")
    genre = models.CharField(max_length = 50)
    origin = models.CharField(max_length = 50)
    image = models.TextField(default = "Artist Image")
    votes = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'
        ordering = ['name']

class Album(models.Model):
    
    name = models.CharField(max_length = 100)
    length = models.CharField(max_length = 7)
    year = models.DateField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    image = models.TextField(default = "Album Image")
    votes = models.IntegerField(default = 1)
    
    def __str__ (self):
        return self.name 

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['name']

class Song(models.Model):
    
    name = models.CharField(max_length = 50)
    number = models.IntegerField()
    length = models.CharField(max_length = 7)
    artist = models.ForeignKey(Band, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    votes = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'
        ordering = ['number']