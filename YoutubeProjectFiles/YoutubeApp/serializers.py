from _typeshed import SupportsNoArgReadline
from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['videoId', 'content', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['replies', 'comment']
