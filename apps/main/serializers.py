from rest_framework import serializers
from .models import Notice, Comment

class NoticeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Notice

class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment