from django.db import models
from articles.models import Articles

class FeaturedArticles(models.Model):
    name = models.CharField(max_length=50, null=True)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE,related_name='featured_articles')

    def __str__(self):
        return f'Featured articles: {self.name}'

    class Meta:
        verbose_name_plural = 'Featured Aritlces'