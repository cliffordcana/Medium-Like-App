from django.shortcuts import render
from rest_framework import generics, response, status, permissions
from .models import RelatedArticles
from .serializers import RelatedArticlesSerializer

class RelatedArticlesList(generics.ListAPIView):
    serializer_class = RelatedArticlesSerializer
    permissions = (permissions.AllowAny, )
    queryset = RelatedArticles.objects.all()

    #TODO: def get_queryset(self):
