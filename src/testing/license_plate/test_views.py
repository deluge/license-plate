class TestLicensePlateValidatorView:
    def test_post_status_200(self, client):
        data = {"license_plate": "B-WE 1234"}
        response = client.post("/validator/", data=data)

        assert response.status_code == 200
        assert response.json() == {
            "is_valid": True,
            "errors": {},
            "license_plate": "B-WE1234",
        }

    def test_post_status_400(self, client):
        data = {"license_plate": "B-WE 1234567"}
        response = client.post("/validator/", data=data)

        assert response.status_code == 400
        assert response.json() == {
            "is_valid": False,
            "errors": {
                "license_plate": ["Ensure this field has no more than 11 characters."]
            },
            "license_plate": "B-WE 1234567",
        }


class TestLicensePlateValidatorHtmlView:
    def test_get(self, client):
        response = client.get("/validator-html/")

        assert response.status_code == 200
        assert "is_valid" not in response.context
        assert "serializer" in response.context
        assert "license_plate" not in response.context
        assert response.context["serializer"].data == {"license_plate": ""}

    def test_post_status_200(self, client):
        data = {"license_plate": "B-WE 1234"}
        response = client.post("/validator-html/", data=data)

        assert response.status_code == 200
        assert "is_valid" in response.context
        assert "serializer" in response.context
        assert "license_plate" in response.context
        assert response.context["is_valid"] is True
        assert response.context["serializer"].errors == {}
        assert response.context["license_plate"] == "B-WE1234"

    def test_post_status_400(self, client):
        data = {"license_plate": "B-WE 1234567"}
        response = client.post("/validator-html/", data=data)

        assert response.status_code == 400
        assert "is_valid" in response.context
        assert "serializer" in response.context
        assert "license_plate" in response.context
        assert response.context["is_valid"] is False
        assert response.context["serializer"].errors == {
            "license_plate": ["Ensure this field has no more than 11 characters."],
        }
        assert response.context["license_plate"] == "B-WE 1234567"

    def test_post_empty_form(self, client):
        response = client.post("/validator-html/")

        assert response.status_code == 400
        assert "is_valid" in response.context
        assert "serializer" in response.context
        assert "license_plate" in response.context
        assert response.context["is_valid"] is False
        assert response.context["license_plate"] is None
        assert len(response.context["serializer"].errors) == 1

        errors = response.context["serializer"].errors
        assert "license_plate" in errors
        assert len(errors["license_plate"]) == 1
        assert str(errors["license_plate"][0]) == "This field is required."
