# articles/serializers.py
from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'content', 'hashtag1', 'hashtag2', 'hashtag3', 'created_at', 'updated_at', 'like_count']

class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'author', 'content', 'created_at', 'like_count']
