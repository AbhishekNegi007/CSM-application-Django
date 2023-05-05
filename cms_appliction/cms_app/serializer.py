from rest_framework import serializers
from cms_app.models import Post, Like,User
from pydantic import BaseModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'email']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'description', 'content', 'creation_date',  'user_id']

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['like_id','post_id', 'user_id']