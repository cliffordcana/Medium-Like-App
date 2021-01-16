from rest_framework import generics, permissions, viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticlesSerializer, ArticleDetailSerializer
from .models import Articles
from django.utils import timezone
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404



#TODO: REFACTOR CODE
class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticlesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'slug']
    

    def get_queryset(self):
        try:
            return Articles.objects.filter(
                date_posted__lte=timezone.now())#.order_by('-date_posted)
        except Articles.DoesNotExist:
            return Response('Article not found', status=status.HTTP_404_NOT_FOUND)

#TODO: REFACTOR CODE
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    permissions = (permissions.AllowAny, )
    lookup_field = 'slug'

    def get_queryset(self):
        try:
            return Articles.objects.all()
        except Articles.DoesNotExist:
            return Response('Article not found', status=status.HTTP_404_NOT_FOUND)
