from tkinter import E
from rest_framework import serializers
from .models import FriendshipStatus
from authentication.models import User

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name']

class FriendshipStatusSerializer(serializers.ModelSerializer):
    requestor = UsersSerializer(read_only=True)
    requestTo = UsersSerializer(read_only=True)
    class Meta:
        model = FriendshipStatus
        fields = ['id', 'requestor', 'requestTo', 'dateAndTime', 'status']
        depth = 1 
        

