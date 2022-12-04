import pytest
from rest_framework.serializers import ValidationError

from app.license_plate.serializers import LicensePlateSerializer


class TestLicensePlateSerializer:
    def test_validate_license_plate(self):
        serializer = LicensePlateSerializer()
        result = serializer.validate_license_plate("b-Et 1234")

        assert result == "B-ET1234"

    def test_validate_license_plate_raise_error(self):
        serializer = LicensePlateSerializer()

        with pytest.raises(ValidationError):
            serializer.validate_license_plate("bEt1234")
