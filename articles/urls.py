from django.urls import path
from .views import ArticleListView, ArticleDetailView
from rest_framework.routers import DefaultRouter

app_name = 'backend'

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<slug>/', ArticleDetailView.as_view(), name='article-detail'),
    #path('articles/<slug>/', ArticleDetailView.as_view()),
]
