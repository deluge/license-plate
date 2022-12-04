import logging
import os
import tempfile

from app.conf.global_settings import *


SECRET_KEY = "NOSECRETNOCRYATLEASTIFITSJUSTABOUTTESTS"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = True

LANGUAGE_CODE = "en"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "test",
        "KEY_PREFIX": "testrunner",
    }
}

MEDIA_ROOT = tempfile.mkdtemp()
STATIC_ROOT = tempfile.mkdtemp()

logging.disable(logging.CRITICAL)

INSTALLED_APPS += ["testing"]
