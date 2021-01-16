from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import FeaturedArticles
from .serializers import FeaturedArticlesSerializer

class FeaturedArticlesList(generics.ListAPIView):
    permissions = (permissions.AllowAny, )
    serializer_class = FeaturedArticlesSerializer

    def get_queryset(self):
        try:
            return FeaturedArticles.objects.all()
        except FeaturedArticles.DoesNotExist:
            return Response('Article not found', status=status.HTTP_404_NOT_FOUND)
