from django.db import models
from articles.models import Articles

class Category(models.Model):
    category = models.CharField(max_length=40)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'categories'