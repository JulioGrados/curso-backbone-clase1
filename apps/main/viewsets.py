from rest_framework import viewsets
from .models import Notice, Comment
from .serializers import NoticeSerializer, CommentSerializer

class NoticeViewSet(viewsets.ModelViewSet):

	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer

class CommentViewSet(viewsets.ModelViewSet):

	queryset = Comment.objects.all()
	serializer_class = CommentSerializer