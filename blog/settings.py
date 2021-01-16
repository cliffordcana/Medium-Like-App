import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1!o_mli6hs%v$+22j2)2kppag3%xwtirc-3gphc&7!7etz^4p&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'articles.apps.ArticlesConfig',
    'category.apps.CategoryConfig',
    'comments.apps.CommentsConfig',
    'django_social.apps.DjangoSocialConfig',
    'featured_articles.apps.FeaturedArticlesConfig',
    'related_articles.apps.RelatedArticlesConfig',
    'contact.apps.ContactConfig',
    'users.apps.UsersConfig',

    'tinymce',

    # django-rest-framework modules
    'rest_framework',
    'rest_framework.authtoken',
    
    # dj_rest_auth modules
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # django-allauth modules
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    #django social
    'social.apps.django_app.default',
    'social_django',
    
    # CORS for React (Cross-Origin Resource Sharing)
    'corsheaders',

    'django_filters',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'Cliffordnew123!',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication', 
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    #'DATETIME_FORMAT': "%Y-%m-%d | %H: 00",
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'users.CustomUser'

#APPEND_SLASH=False #RESEARCH OPTIONAL


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of allauth
    'django.contrib.auth.backends.ModelBackend',
    # allauth specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    #facebook social
    'social_core.backends.facebook.FacebookOAuth2',
]

#SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("SOCIAL_AUTH_FACEBOOK_KEY")
#SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("SOCIAL_AUTH_FACEBOOK_SECRET")
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none' #mandatory
SITE_ID = 2



REST_USE_JWT=True
#JWT_AUTH_COOKIE = 'jwt-token'

REST_AUTH_SERIALIZERS = {
        'USER_DETAILS_SERIALIZER': 'users.serializers.UserDetailSerializer',
        #'TOKEN_SERIALIZER ': 'users.utils.MyTokenObtainPairView',
        #'JWT_SERIALIZER ': 'users.serializers.UserRegistrationSerializerWithToken',
}

REST_AUTH_REGISTER_SERIALIZERS = {
        'REGISTER_SERIALIZER': 'users.serializers.UserRegistrationSerializerWithToken',
        'USER_DETAILS_SERIALIZER': 'users.serializers.UserDetailSerializer',
}


#JWT_EXPIRATION_DELTA: force logout if there was no refresh in last 3 days
#JWT_REFRESH_EXPIRATION_DELTA: force logout after 14 days passed
import datetime

JWT_AUTH = {
    #'JWT_SECRET_KEY': get_private("SECRET_KEY_JWT"),
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=14),
    #'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_handler',
}



SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
            'givenName',
            'imageUrl'
            ],
            'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'gender'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v9.0',
    }
}


SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True, # IMPORTANT
    'BLACKLIST_AFTER_ROTATION': True, # IMPORTANT
    'UPDATE_LAST_LOGIN': True,
}

SOCIALACCOUNT_ADAPTER = 'users.adapter.CustomSocialAccountAdapter'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

