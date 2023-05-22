from rest_framework import serializers
from .models import Post, Comment, Reply
from authentication.models import User


class UsersSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username']
    depth = 1
class ReplySerializer(serializers.ModelSerializer):
    author = UsersSerializer(read_only=True)
    class Meta:
        model = Reply
        fields = ['id','reply','created_on', 'author','reply']
    depth = 1  
class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(read_only=True, many=True)
    author = UsersSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id','created_on', 'author','comment', 'replies']
    depth = 3

class PostSerializer(serializers.ModelSerializer):
    author = UsersSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    likes = UsersSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['id','author','likes','disLikes','body', 'created_on','album_id', 'track_id', 'album_title','track_title', 'artist_name', 'album_image', 'preview_track', 'comments']
        depth = 1

