from collections import UserString
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import FriendshipStatusSerializer
from .serializers import UsersSerializer
from .models import FriendshipStatus
from authentication.models import User
from django.db.models import Q 
from difflib import get_close_matches


@api_view(['POST', 'PATCH', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def friend_request(request, pk=''):
  print('User', f"{int(request.user.id)} {request.user.email} {request.user.username}")       
  if request.method == 'POST':
    print('*******************************')
    requestor = get_object_or_404(User, pk = request.user.id)
    requestTo = get_object_or_404(User, pk = pk)
    serializer = FriendshipStatusSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(requestor= requestor, requestTo=requestTo)
      return Response(serializer.data, status=status.HTTP_200_OK)      
  if request.method == 'PATCH':
    friend_request = get_object_or_404(FriendshipStatus, pk=pk)
    serializer = FriendshipStatusSerializer(friend_request, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)
  if request.method == 'GET':
    print('*************pk******************', pk)
    user = get_object_or_404(User, pk = pk)
    friendIds = FriendshipStatus.objects.filter(requestor = pk).filter(status = 'accepted') | FriendshipStatus.objects.filter(requestTo = pk).filter(status = 'accepted').only('requestor', 'requestTo')
    friends = []
    for item in friendIds:
      if item.requestor == user:
        friends.append(item.requestTo)
      elif item.requestTo == user:
        friends.append(item.requestor)
    serializer = UsersSerializer(friends, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)  
  if request.method == 'DELETE':
    friend = get_object_or_404(User, pk=pk)
    print('***OOOOOOO****pk:', pk)
    print('*******user:', request.user.username)
    friendRequest = FriendshipStatus.objects.filter(requestor = request.user.id) | FriendshipStatus.objects.filter(requestTo = request.user.id).only('requestor', 'requestTo')
    for item in friendRequest:
      if item.requestTo == friend or item.requestor == friend:
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def friend_request_pending(request):
  if request.method == 'GET':
    friendIds = FriendshipStatus.objects.filter(requestTo = request.user.id).filter(status = 'requested').only('requestor')
    pendingFriendsSerializer = FriendshipStatusSerializer(friendIds, many=True) 
    return Response(pendingFriendsSerializer.data, status=status.HTTP_200_OK)   
  return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
  if request.method == 'GET':
    allUsersExceptLoggedIn = User.objects.all().exclude(id = request.user.id).exclude(username = "admin")
    serializer = UsersSerializer(allUsersExceptLoggedIn, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_users(request, query=''):
    if request.method == 'GET':
        qs = User.objects.all()
        for user in query.split():
          qs = qs.filter( Q(first_name__icontains = user) | Q(last_name__icontains = user))
        serializer = UsersSerializer(qs, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)       
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)