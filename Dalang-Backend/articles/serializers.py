# articles/serializers.py
from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'author', 'author_username', 
            'content', 'hashtag1', 'hashtag2', 'hashtag3', 
            'created_at', 'updated_at', 'like_count', 'comment_count'
        ]

class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'like_count', 'author', 'author_username'] # article, author 제외 -> 짜피 정해져 있으니깐!
        read_only_fields = ['author']  # 읽기 전용 필드
