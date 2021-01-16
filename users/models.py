from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount
from allauth.account.signals import user_signed_up


def upload_dir_path(instance, filename):
    return 'file_upload_{0}/{1}'.format(instance.id, filename)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    nickname = models.CharField(max_length=30, default='User')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #for social
    #TODO: change null and blank to false
    picture = models.URLField(null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True) 
    gender = models.CharField(max_length=10, null=True, blank=True) 

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager() 

    # console field name for python manage.py createsuperuser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, users):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def get_absolute_url(self):
        return '/users/%i' % self.pk

        
    class Meta:
        verbose_name_plural = 'Custom Users'

