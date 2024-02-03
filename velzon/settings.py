"""
Django settings for velzon project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import ldap

import logging

import os

from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j%^*y0krq5^-#3lggoecxw!d7ad_gqkab3t5w17&0w06+qf8+8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.31.191', '127.0.0.1', 'localhost','192.168.0.100', '.vercel.app', '.now.sh']


# Application definition
DEFAULT_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "corsheaders",
    # "knox",
    
    ]
LOCAL_APPS = [
    "dashboards",
    "apps",
    "main_site",
    "layouts",
    "components",
    "pages",
    "directories",
    "project",
    "knox",
    "rest_framework",
    "reactapp",
    ] 
THIRDPARTY_APPS = [
    
    # Crispy Forms
    "crispy_forms",
    'crispy_bootstrap5',

    
    # All Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'allauth.socialaccount.providers.google', 
     
    # Google Providers
    'multiselectfield',
]

INSTALLED_APPS = DEFAULT_APPS +LOCAL_APPS +THIRDPARTY_APPS

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ROOT_URLCONF = 'velzon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build'),
            os.path.join(BASE_DIR, 'templates'),  # Add this line
            ],
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

AUTHENTICATION_BACKENDS = [
    # other backends...
    'allauth.account.auth_backends.AuthenticationBackend',
    # other backends...
]

# AUTHENTICATION_BACKENDS = [
#     'django_auth_ldap.backend.LDAPBackend',
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',

    


# ]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

WSGI_APPLICATION = 'velzon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
       
#     }
# }
import environ

env = environ.Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase.db',
        'USER': env.str('DB_USER', default=''),
        'PASSWORD': env.str('DB_PASSWORD', default=''),
        'HOST': env.str('DB_HOST', default=''),
        'PORT': env.int('DB_PORT', default=5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True
  

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]
# STATIC_ROOT = [os.path.join(BASE_DIR,"static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static_cdn"),
    os.path.join(BASE_DIR,'build','static'),
    os.path.join(BASE_DIR,'staticfiles_build','static'),
    # os.path.join(BASE_DIR,"static"),

]
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#  Messages customize

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


# SMTP Configure
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.mailtrap.io"
# EMAIL_PORT = 2525
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""
# DEFAULT_FROM_EMAIL = ""

#  All Auth Configurations

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "account_login"
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True

ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_LOGIN_ON_GET = False

# All Auth Forms Customization 

ACCOUNT_FORMS = {
    "login": "velzon.forms.UserLoginForm",
    "signup": "velzon.forms.UserRegistrationForm",
    "change_password": "velzon.forms.PasswordChangeForm",
    "set_password": "velzon.forms.PasswordSetForm",
    "reset_password": "velzon.forms.PasswordResetForm",
    "reset_password_from_key": "velzon.forms.PasswordResetKeyForm",
}

SOCIALACCOUNT_QUERY_EMAIL = True


SITE_ID = 2

# Provider Configurations
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
   }

}




# # LDAP Configuration

# from django_auth_ldap.config import LDAPSearch

# # LDAP server URI
# AUTH_LDAP_SERVER_URI = "ldap://192.168.31.250:389"

# # Bind DN and password (the account used to connect to the LDAP server)
# AUTH_LDAP_BIND_DN = "CN=Administrator,CN=Users,DC=qtoh,DC=local"
# AUTH_LDAP_BIND_PASSWORD = "Cow&Gate"

# # User search configuration
# AUTH_LDAP_USER_SEARCH = LDAPSearch(
#     "OU=Estimators,DC=qtoh,DC=local",
#     ldap.SCOPE_SUBTREE,
#     "(sAMAccountName=%(user)s)"
# )

# # User attribute mapping (LDAP attribute to Django User model field)
# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     "mail":"mail",
# }


# def user_post_save(user, ldap_user, **kwargs):
#     if ldap_user.get("department") == "Estimators":
#         user.is_staff = True
#     user.save()
# AUTH_LDAP_USER_POST_SAVE = "myapp.user_post_save"
# # Hook this function to the AUTH_LDAP_USER_MIRROR_CALLBACK
# AUTH_LDAP_USER_MIRROR_CALLBACK = user_post_save

# logger = logging.getLogger('django_auth_ldap')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_ALL_ORIGINS = True  
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]





# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         # 'rest_framework.authentication.BasicAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication',
#         'Knox.auth.TokenAuthentication'

#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated'
#     ]
# }

# urlpatterns += statuc(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)