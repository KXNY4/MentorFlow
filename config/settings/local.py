import sys

from .base import *
from .base import env

SECRET_KEY = env("SECRET_KEY", default="django-insecure-vud%um1%&570=^#0bdet92+9jrgkttte(@lub!2e9@+qqlc#$z`")

DEBUG = env("DEBUG", default=True)

INTERNAL_IPS = env.list("INTERNAL_IPS", default="127.0.0.1")

INSTALLED_APPS += [
        "django_extensions",
    ]

TESTING = "test" in sys.argv
if not TESTING:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]


# EMAIL
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "Mentor FLow prod. <MentorMailFLow@gmail.com>"