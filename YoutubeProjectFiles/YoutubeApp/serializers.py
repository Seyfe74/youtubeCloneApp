from _typeshed import SupportsNoArgReadline
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['id', 'content', 'date', 'likes', 'dislikes', 'replies']