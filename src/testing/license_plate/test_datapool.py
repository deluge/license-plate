from app.license_plate.datapool import LicensePlatePool


class TestLicensePlatePool:
    def test_city_plate_exists(self):
        pool = LicensePlatePool()

        assert pool.city_plate_exists("LDS") is True

    def test_city_plate_not_exists(self):
        pool = LicensePlatePool()

        assert pool.city_plate_exists("ÖÖÖ") is False
