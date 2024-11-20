from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

# 게시글 목록 뷰
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 게시글 생성 뷰
class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# 게시글 상세 뷰
class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 게시글 수정 뷰
class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            self.permission_denied(self.request, message="You do not have permission to edit this article.")
        serializer.save()

# 게시글 삭제 뷰
class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            self.permission_denied(self.request, message="You do not have permission to delete this article.")
        instance.delete()

# 특정 게시판의 모든 댓글 조회 뷰
class CommentListView(APIView):
    def get(self, request, article_pk):
        comments = Comment.objects.filter(article_id=article_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 댓글 생성 뷰
class CommentCreateView(generics.CreateAPIView):
    # queryset = Comment.objects.all()
    # serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     article = get_object_or_404(Article, pk=self.kwargs['article_pk'])
    #     serializer.save(author=self.request.user, article=article)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # 게시글을 가져오고 없으면 404 반환
        article = get_object_or_404(Article, pk=self.kwargs.get('article_pk'))
        # 작성자와 게시글을 설정하여 저장
        serializer.save(
            author=self.request.user,
            article=article
        )

# 댓글 상세 뷰
class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 댓글 수정 뷰
class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            self.permission_denied(self.request, message="You do not have permission to edit this comment.")
        serializer.save()

# 댓글 삭제 뷰
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            self.permission_denied(self.request, message="You do not have permission to delete this comment.")
        instance.delete()

# 게시글 좋아요 추가/취소 뷰
class ArticleLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        if user in article.likes.all():
            article.likes.remove(user)
            liked = False
        else:
            article.likes.add(user)
            liked = True

        return Response({
            'liked': liked,
            'like_count': article.likes.count()
        }, status=status.HTTP_200_OK)

# 댓글 좋아요 추가/취소 뷰
class CommentLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, article_pk, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = request.user

        if user in comment.likes.all():
            comment.likes.remove(user)
            liked = False
        else:
            comment.likes.add(user)
            liked = True

        return Response({
            'liked': liked,
            'like_count': comment.likes.count()
        }, status=status.HTTP_200_OK)
