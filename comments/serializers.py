from rest_framework import serializers
from .models import Comment
from articles.models import Articles

class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    picture = serializers.CharField(source='user.picture', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'slug',
            'article',
            'user',
            'comment',
            'comment_date',
            'parent',
            'nickname',
            'picture',
            'first_name' 
        )
    
class CommentDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'slug',
            'article',
            'user',
            'comment',
            'comment_date',
            'parent',
            #'nickname'
        )
        
