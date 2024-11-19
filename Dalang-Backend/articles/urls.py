from django.urls import path
from .views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
