import pytest
from rest_framework.serializers import ValidationError

from app.license_plate.validators import LicensePlateValidator


class TestLicensePlateValidator:
    def test_is_valid(self):
        validator = LicensePlateValidator()
        result = validator("b-Et 1234")

        assert result == "B-ET1234"

    def test_invalid_numbers_of_characters(self):
        validator = LicensePlateValidator()

        with pytest.raises(ValidationError) as exc:
            validator("LDS-ET 1234567")

        expected_message = (
            "Invalid number of characters. Maximum 8 characters are allowed."
        )
        assert exc.value.args[0] == expected_message

    def test_invalid_format(self):
        validator = LicensePlateValidator()

        with pytest.raises(ValidationError) as exc:
            validator("LDSET 12")

        expected_message = (
            "Invalid format. Please enter one of the following: 'B-ER 1234' "
            "or 'B-ER1234'"
        )
        assert exc.value.args[0] == expected_message

    def test_license_plate_not_in_dataset(self):
        validator = LicensePlateValidator()

        with pytest.raises(ValidationError) as exc:
            validator("ÖÖ-TU 12")

        assert exc.value.args[0] == "ÖÖ is not a valid german city or district."
