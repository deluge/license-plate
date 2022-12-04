import os

from django.utils.translation import gettext_lazy as _


SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(SRC_DIR)

SECRET_KEY = ""
DEBUG = False

ALLOWED_HOSTS = []

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "license_plate",
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "app.license_plate.apps.LicensePlateConfig",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "web", "static")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = os.path.join(BASE_DIR, "web", "media")
MEDIA_URL = "/media/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "templates/locale"),
]

LANGUAGE_CODE = "en"
LANGUAGES = [("en", _("English")), ("de", _("German"))]
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
        "django": {
            "level": "WARNING",
            "handlers": ["console"],
        },
    },
}
