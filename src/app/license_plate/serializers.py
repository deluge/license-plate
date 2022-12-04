from rest_framework import serializers

from app.license_plate.validators import LicensePlateValidator


class LicensePlateSerializer(serializers.Serializer):
    license_plate = serializers.CharField(max_length=11)

    def validate_license_plate(self, value):
        validator = LicensePlateValidator()
        return validator(value)
