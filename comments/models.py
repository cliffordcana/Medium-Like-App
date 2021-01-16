from django.db import models
from django.conf import settings
from articles.models import Articles

class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', 
        on_delete=models.CASCADE, null=True, blank=True, related_name='replies'
    )

    @property
    def slug(self):
        return self.article.slug

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name_plural = 'comments'

        