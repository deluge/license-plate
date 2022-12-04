import re

from django.utils.translation import gettext
from rest_framework.serializers import ValidationError

from app.license_plate.datapool import LicensePlatePool


LICENSE_PLATE_RE = re.compile(
    r"^([A-ZÖÜÄ]{1,3})-([A-Z]{1,2})(?:\s)?([1-9]{1}[0-9]{,3})$"
)
NON_ALPHANUMERIC_RE = re.compile(r"[^0-9A-ZÖÜÄ]")


class LicensePlateValidator:
    def __init__(self):
        self.max_characters = 8

    def __call__(self, value):
        license_plate = value.upper()

        if len(NON_ALPHANUMERIC_RE.sub("", license_plate)) > self.max_characters:
            raise ValidationError(
                gettext(
                    "Invalid number of characters. Maximum {} characters are allowed."
                ).format(self.max_characters)
            )

        result = LICENSE_PLATE_RE.search(license_plate)
        if result is None:
            raise ValidationError(
                gettext(
                    "Invalid format. Please enter one of the following: 'B-ER 1234' "
                    "or 'B-ER1234'"
                )
            )

        city, custom, number = result.groups()

        if not LicensePlatePool().city_plate_exists(city):
            raise ValidationError(
                gettext("{} is not a valid german city or district.").format(city)
            )

        return f"{city}-{custom}{number}"
