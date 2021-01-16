
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import CustomUser
from allauth.socialaccount.models import SocialLogin, SocialToken
import json
import facebook
import requests

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form):
        user = super(CustomSocialAccountAdapter, self).save_user(request, sociallogin, form)

        access_token = SocialToken.objects.get(
            account__user=user, account__provider='facebook'
        )
        
        response = requests.get(f'https://graph.facebook.com/me?access_token={access_token.token}&fields=id,name,gender,picture')
        print('response', response.json())

        picture_url = response.json()['picture']['data']['url']
        name = response.json()['name']
        #gender = response.json()['gender']

        user.picture = picture_url
        user.name = name

        print('picture_url', picture_url)
        print('user.name', user.name)

        user.save()
        

