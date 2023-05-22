from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from authentication.models import User
from .models import Album

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name',]




class AlbumSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    album_id = serializers.IntegerField(required=True, validators=[
                                   UniqueValidator(queryset=Album.objects.all(), message="My custom error",)])
    class Meta:
        model = Album
        fields = ['id','user', 'album_id', 'title', 'artist', 'image', 'preview', 'preview_title']
        depth = 1
