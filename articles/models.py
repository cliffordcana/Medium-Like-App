from django.db import models
from datetime import timedelta
from django.utils import timezone
from PIL import Image
from django.contrib.auth import get_user_model
from image_cropping import ImageRatioField
#from comments.models import Comment

User = get_user_model()

def upload_dir_path(instance, filename):
    return 'file_upload_{0}/{1}'.format(instance.author.id, filename)

class Articles(models.Model):
    PYTHON = 'P'
    DJANGO = 'D'
    DJANGO_REST_FRAMEWORK = 'DRF'
    JAVASCRIPT = 'JS'
    REACT = 'R'
    MYSQL = 'M'
    HTML = 'H'
    CSS = 'C'
    RELATED_ARTICLES = 'RA'
    #FEATURED_ARTICLES = 'FA'
    ARTICLE_CHOICES = [
        (PYTHON, 'Python'),
        (DJANGO, 'Django'),
        (DJANGO_REST_FRAMEWORK, 'Django Rest Framework'),
        (JAVASCRIPT, 'Javascript'),
        (REACT, 'React'),
        (MYSQL, 'MySQL'),
        (HTML, 'HTML'),
        (CSS, 'CSS'),
        (RELATED_ARTICLES, 'RELATED_ARTICLES'),
        #(FEATURED_ARTICLES, 'FEATURED_ARTICLES'),
        
    ]
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=250, null=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_dir_path, null=True, blank=True)
    cropping = ImageRatioField('image', '1000x1000')
    article_choices = models.CharField(max_length=3, choices=ARTICLE_CHOICES, default=PYTHON)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def view_count(self):#TODO:
        return Articles.objects.filter(articles=self).count()

    '''@property
    def get_comment(self):
        return Articles.comments.id'''

    '''@property
    def comment_count(self):    #TODO:
        return Comment.objects.fiter(articles=self).count()'''
    
    def was_posted_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.date_posted <= now

    was_posted_recently.admin_order_field = 'date_posted'
    was_posted_recently.boolean = True
    was_posted_recently.short_description = 'Recently posted?'
    
    class Meta:
        verbose_name_plural = 'articles'        



'''
#TODO:
class Tag(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, 
                related_name='tags', related_query_name='tag')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'tags'

#TODO:
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

TODO:class ArticlesManager(models.Model):  https://docs.djangoproject.com/en/3.1/topics/db/managers/
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            result_list = []
            for row in cursor.fetch.all():
                res = self.model(id=row[0], )'''

