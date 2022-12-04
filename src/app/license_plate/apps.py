from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LicensePlateConfig(AppConfig):
    name = "app.license_plate"
    verbose_name = _("License plate validator")
