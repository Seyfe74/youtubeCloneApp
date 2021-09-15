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
        reply = Reply.objects.all()
        serializer = CommentSerializer(comment, many=True)
        serializerReply = ReplySerializer(reply, many=True)

