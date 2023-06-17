from rest_framework import serializers
from .models import Post, Comment
from authorization.serializers import GetUserSerializer

class PostSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'

    def get_user_info(self, obj):
        serializer = GetUserSerializer(obj.user)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_user_info(self, obj):
        serializer = GetUserSerializer(obj.user)
        return serializer.data