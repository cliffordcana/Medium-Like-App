from .views import RelatedArticlesList
from django.urls import path

app_name = 'related_articles'

urlpatterns = [
    path('related-articles/', RelatedArticlesList.as_view())
]
