from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.http import HttpResponse
from comments.serializers import CommentSerializer
from .models import Articles


User = get_user_model()

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        #lookup_fields = ['pk', 'slug']
        fields = (
            'id',
            #TODO:'comment_count',
            'title',
            'short_description',
            'content',
            'slug',
            'date_posted',
            'date_updated',
            'image',
            'article_choices',
            'author',
        )

class ArticleDetailSerializer(serializers.ModelSerializer):
    article_comments = CommentSerializer(many=True, read_only=True, source='comments')
    #nickname = serializers.CharField(source='author.nickname', read_only=True)
    #article = serializers.SerializerMethodField()
    #TODO:nickname = UserNicknameSerializer(many=True, read_only=True)

    class Meta:
        model = Articles
        fields = (
            'id',
            #TODO:'parent',
            #'article',
            #todo:'nickname',
            'title',
            'short_description',
            'content',
            'slug',
            'date_posted',
            'date_updated',
            'image',
            'article_choices',
            'author',
            'article_comments',
        )
    
    