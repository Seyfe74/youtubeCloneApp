from django.http.response import Http404
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentDetail(APIView):
    def get(self, request, videoId):
        comments = Comment.objects.filter(videoId=videoId)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

#TODO: Add routes (functions) for liking and disliking a comment (will increase the like or dislike property on Comment by 1 every time the endpoint is requested)


class ReplyList(APIView):
    def get(self, request,comment_id):
        #TODO: Change this so it only gets replies for a specific comment
        reply = Reply.objects.filter(comment_id = comment_id)
        serializerReply = ReplySerializer(reply, many=True)
        return Response(serializerReply.data)

    def post(self, request, comment):
        # make sure this is tied to a comment!
        serializerReply = ReplySerializer(data=request.data)
        if serializerReply.is_valid():
            serializerReply.save()
            return Response(serializerReply.data, status=status.HTTP_201_CREATED)
        return Response(serializerReply.errors, status=status.HTTP_400_BAD_REQUEST)
