from rest_framework import serializers
from articles.serializers import ArticlesSerializer
from .models import RelatedArticles

class RelatedArticlesSerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(read_only=True)

    class Meta:
        model = RelatedArticles

        fields = (
            'id',
            'name',
            'articles'
        )

