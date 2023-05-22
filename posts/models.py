from django.db import models
from authentication.models import User
from django.utils import timezone

class Post(models.Model):
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, blank=True, related_name='likes')
  disLikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
  album_id = models.IntegerField()
  track_id = models.IntegerField(blank=True, null=True)
  album_title = models.CharField(max_length=255)
  track_title = models.CharField(max_length=255)
  artist_name = models.CharField(max_length=255)
  album_image = models.CharField(max_length=255)
  preview_track = models.CharField(max_length=255)

class Comment(models.Model):
  comment = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

class Reply(models.Model):
  reply = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies')
