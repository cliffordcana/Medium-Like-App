from rest_framework import serializers
from .models import Category
from articles.serializers import ArticlesSerializer
from articles.models import Articles

class CategorySerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(read_only=True)
    #TODO:nickname = serializers.CharField(source='author.nickname')

    class Meta:
        model = Category
        fields = (
            'id',
            'category',
            #:TODO:'nickname',
            'articles',
        )
    
    def create(self, validated_data):
        articles_data = validated_data.pop('articles')
        category = Category.objects.create(**validated_data)
        for article_data in articles_data:
            Articles.objects.create(category=category, **article_data)
        return category
