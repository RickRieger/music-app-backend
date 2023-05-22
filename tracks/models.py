from django.db import models
from authentication.models import User


class Track(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  track_id = models.IntegerField(unique=True)
  album = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  preview = models.CharField(max_length=255)
 