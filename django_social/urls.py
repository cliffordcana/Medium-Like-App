from django.urls import path
from .views import FacebookLoginView, GoogleLoginView, TwitterLoginView

app_name = 'django_social'

urlpatterns = [
    path('facebook-login/', FacebookLoginView.as_view()),
    path('google-login/', GoogleLoginView.as_view()),
    path('twitter-login/', TwitterLoginView.as_view()),
]
