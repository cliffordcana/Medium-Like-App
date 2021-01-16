from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('articles.urls')), 
    path('api/', include('comments.urls')), 
    path('api/', include('users.urls')),
    path('api/', include('category.urls')),
    path('api/', include('featured_articles.urls')),
    path('api/', include('related_articles.urls')),
    path('api/', include('django_social.urls')),
    path('api/', include('contact.urls')),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    #path('/contact-me/', ContactListView.as_view()),

    #TODO:
    path('tinymce/', include('tinymce.urls')),

    #TODO:
    url(r'^jwt-auth/$', obtain_jwt_token),
    url(r'^jwt-auth/refresh/$', refresh_jwt_token),
    url(r'^jwt-auth/verify/$', verify_jwt_token),

    path('accounts/', include('allauth.urls')),
    path('', include('social_django.urls', namespace='social'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
