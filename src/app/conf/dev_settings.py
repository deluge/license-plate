from app.conf.global_settings import *


SECRET_KEY = "LOCALDEVELOPMENTSECRETKEYISINSECURE"

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "127.0.0.1",
        "NAME": "license_plate_dev",
        "USER": "postgres",
        "PASSWORD": "postgres",
    }
}
