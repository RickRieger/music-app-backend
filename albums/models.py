from django.db import models
from authentication.models import User


class Album(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  album_id = models.IntegerField(unique=True)
  title = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  preview = models.CharField(max_length=255)
  preview_title = models.CharField(max_length=255)

