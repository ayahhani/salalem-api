from django.db import models

class VinylModel(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='profile_image', blank=True)