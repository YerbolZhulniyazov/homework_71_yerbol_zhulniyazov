from rest_framework import serializers
from posts.models import Post, Like, Comment


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'author', 'post', 'is_like', 'created_at', 'changed_at')
        read_only_fields = ('id', 'created_at', 'changed_at')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'image', 'created_at')
        read_only_fields = ('id', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created_at', 'changed_at')
        read_only_fields = ('id', 'created_at', 'changed_at')
