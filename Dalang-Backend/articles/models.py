from django.db import models
from django.conf import settings
from accounts.models import User

# Article Model
from django.db import models

# 게시글 모델
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # 작성자 필드
    content = models.TextField()
    hashtag1 = models.CharField(max_length=15, null=True, blank=True)
    hashtag2 = models.CharField(max_length=15, null=True, blank=True)
    hashtag3 = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)  # 좋아요 필드 추가

    def __str__(self):
        return self.title

# Comment Model
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)  # 좋아요 필드 추가

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"
