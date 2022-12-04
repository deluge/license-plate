from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from app.license_plate.views import (
    LicensePlateValidatorHtmlView,
    LicensePlateValidatorView,
)


router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("validator/", LicensePlateValidatorView.as_view()),
    path("validator-html/", LicensePlateValidatorHtmlView.as_view()),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)
