from django.test import TestCase
from django.utils import timezone
from .models import Articles, Comment
from datetime import timedelta

class ArticleModelTests(TestCase):
    """TODO: APITestCase for rest
    """
    
    def test_was_posted_recently_with_old_article(self):
        """
            was_posted_recently() returns False for questions whose date_posted
            is older than 1 day.
        """
        time = timezone.now() - timedelta(days=1, seconds=1)
        old_article = Articles(date_posted=time)
        self.assertIs(old_article.was_posted_recently(), False)
        
    
    def test_was_posted_recently_with_new_article(self):
        """
            was_posted_recently() returns True for questions whose date_posted
            is within the last day.
        """
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_article = Articles(date_posted=time)
        self.assertIs(recent_article.was_posted_recently(), True)

