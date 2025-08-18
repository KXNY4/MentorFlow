import os
from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(".envs", ".local", "django.env"))

APP_DIR = BASE_DIR / "apps"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])


# Application definition

INSTALLED_APPS = [
    # DJANGO_APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # THIRD_PARTY_APPS
    "rest_framework",
    "rest_framework_simplejwt",
    "django_celery_results",
    "django_celery_beat",
    # DJANGO_CLEANUP
    "djoser",
    "djcelery_email",
    # LOCAL_APPS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password hashing

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]


# Password validation

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

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DEFAULT USER MODEL

# AUTH_USER_MODEL = "users.User"


# CELERY
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://localhost:6379/0")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_TASK_SEND_SENT_EVENT = True
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

# CELERY RESULT SETTINGS
CELERY_RESULT_EXTENDED = True
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="django-db")
CELERY_CACHE_BACKEND = env("CELERY_CACHE_BACKEND", default="django-cache")

# CELERY BEAT SETTINGS
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": env("SIGNING_KEY", default="dev_secret_key"),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # # Custom
    # "AUTH_COOKIE": "access",
    # "AUTH_COOKIE_MAX_AGE": 60 * 60 * 24 * 7,
    # "AUTH_COOKIE_SECURE": env.bool("AUTH_COOKIE_SECURE", default=False),
    # "AUTH_COOKIE_HTTP_ONLY": True,
    # "AUTH_COOKIE_PATH": "/",
    # "AUTH_COOKIE_SAMESITE": "Lax",
}


DJOSER = {
    "LOGIN_FIELD": "email",
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFORMATION_EMAIL": True,
    "LOGOUT_ON_PASSWORD_CHANGE": False,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_URL": "account/auth/password-reset/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "account/auth/email-reset/{uid}/{token}",
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": env.list(
        "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS",
        default=[
            "http://localhost:3000",
        ],
    ),
    "ACTIVATION_URL": "account/auth/activate/{uid}/{token}",
    "SERIALIZERS": {
    },
    "PERMISSIONS": {
        "user": ["apps.core.permissions.CurrentUserOrReadOnlyPermission"],
        "user_list": ["rest_framework.permissions.AllowAny"],
    },
    "EMAIL": {
        "activation": "apps.users.email.ActivationEmail",
        "confirmation": "apps.users.email.ConfirmationEmail",
        "password_reset": "apps.users.email.PasswordResetEmail",
        "password_changed_confirmation": "apps.users.email.PasswordChangedConfirmationEmail",
        "username_changed_confirmation": "apps.users.email.UsernameChangedConfirmationEmail",
        "username_reset": "apps.users.email.UsernameResetEmail",
    },
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "USERNAME_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "HIDE_USERS": False,
    "TOKEN_MODEL": None,
}


# CACHE

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_CACHE_LOCATION", default="redis://localhost:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}