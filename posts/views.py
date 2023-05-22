from django.shortcuts import get_object_or_404
from xmlrpc.client import ResponseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, ReplySerializer
from friends.models import FriendshipStatus



@api_view(['GET', 'DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def posts(request, pk=''):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        friendIds = FriendshipStatus.objects.filter(requestor = request.user.id).filter(status = 'accepted') | FriendshipStatus.objects.filter(requestTo = request.user.id).filter(status = 'accepted').only('requestor', 'requestTo')

        postFeedIds = []
        
        for item in friendIds:
            if item.requestor == request.user:
               postFeedIds.append(item.requestTo.id)
            elif item.requestTo == request.user:
               postFeedIds.append(item.requestor.id)

        postFeedIds.append(request.user.id)      
        feed = Post.objects.filter(author__in=postFeedIds).order_by('-created_on')
           
        serializer = PostSerializer(feed, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE': 
        post = get_object_or_404(Post, pk=pk) 
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comments(request, postId):
    if request.method == 'POST':
     
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
           
            serializer.save(post_id=postId, author_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def replies(request, pk=''):
    print('======', pk, request)
    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment_id=pk, author_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
      
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def likes(request, id):
    signed_in = request.user
    post = Post.objects.get(id=id)

    if signed_in and post:
        post.likes.add(signed_in)
        return Response("Successful")
    else:
        return Response("Unsuccessful",  status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def disLikes(request, id):
    signed_in = request.user
    post = Post.objects.get(id=id)

    if signed_in and post:
        post.disLikes.add(signed_in)
        return Response("Successful")
    else:
        return Response("Unsuccessful",  status.HTTP_404_NOT_FOUND)


