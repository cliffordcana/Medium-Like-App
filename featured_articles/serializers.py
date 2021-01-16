from rest_framework import serializers
from articles.serializers import ArticlesSerializer
from .models import FeaturedArticles

class FeaturedArticlesSerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(read_only=True)
    
    class Meta:
        model = FeaturedArticles
        fields = ('id', 'name', 'articles')
