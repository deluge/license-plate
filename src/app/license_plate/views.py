from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.license_plate.serializers import LicensePlateSerializer


class LicensePlateValidatorView(APIView):
    def post(self, request, format=None):
        serializer = LicensePlateSerializer(data=request.data)

        is_valid = serializer.is_valid()
        response_status = (
            status.HTTP_200_OK if is_valid else status.HTTP_400_BAD_REQUEST
        )

        response = {
            "is_valid": is_valid,
            "errors": serializer.errors,
        }
        response.update(serializer.data)

        return Response(response, status=response_status)


class LicensePlateValidatorHtmlView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "validation_form.html"

    def get(self, request, format=None):
        serializer = LicensePlateSerializer()
        return Response({"serializer": serializer})

    def post(self, request, format=None):
        serializer = LicensePlateSerializer(data=request.data)

        is_valid = serializer.is_valid()
        response_status = (
            status.HTTP_200_OK if is_valid else status.HTTP_400_BAD_REQUEST
        )

        return Response(
            {
                "serializer": serializer,
                "is_valid": is_valid,
                "license_plate": serializer.data.get("license_plate", None),
            },
            status=response_status,
        )
