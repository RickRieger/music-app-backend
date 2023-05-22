from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from authentication.models import User
from .models import Track

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name',]

class TrackSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    track_id = serializers.IntegerField(required=True, validators=[
                                   UniqueValidator(queryset=Track.objects.all())])
    class Meta:
        model = Track
        fields = ['id','user', 'track_id','album', 'title', 'artist', 'image', 'preview']
        depth = 1
