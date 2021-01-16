from django.contrib.auth.base_user import BaseUserManager
import jwt
from allauth.socialaccount.adapter import get_account_adapter

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, nickname='User', **extra_fields):
        '''
        Creates and saves a User with the given email, nickname and password.
        '''
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            **extra_fields
        )

        user.is_admin = False
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, password, nickname='Admin', **extra_fields):
        '''
        Creates and saves a superuser with the given email, nickname and password.
        '''
        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
            **extra_fields
        )

        user.is_admin = True
        user.save()

        return user
