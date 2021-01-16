from .views import FeaturedArticlesList
from django.urls import path

app_name = 'featured_articles'

urlpatterns = [
    path('featured-articles/', FeaturedArticlesList.as_view())
]
