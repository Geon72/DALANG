from django.urls import path
from .views import (
    ArticleListView, ArticleCreateView, ArticleDetailView,
    ArticleUpdateView, ArticleDeleteView, ArticleLikeView,
    CommentCreateView, CommentDetailView, CommentUpdateView,
    CommentDeleteView, CommentLikeView
)

urlpatterns = [
    # 게시글 URL 패턴
    path('', ArticleListView.as_view(), name='article_list'),  # 게시글 목록
    path('create/', ArticleCreateView.as_view(), name='article_create'),  # 게시글 생성
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),  # 게시글 상세
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),  # 게시글 수정
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),  # 게시글 삭제 -> 요청 METHOD : DELETE
    path('<int:article_pk>/like/', ArticleLikeView.as_view(), name='article_like'),  # 게시글 좋아요

    # 댓글 URL 패턴
    path('<int:article_pk>/comments/create/', CommentCreateView.as_view(), name='comment_create'),  # 댓글 생성
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),  # 댓글 상세
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),  # 댓글 수정
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),  # 댓글 삭제
    path('<int:article_pk>/comments/<int:comment_pk>/like/', CommentLikeView.as_view(), name='comment_like'),  # 댓글 좋아요
]
