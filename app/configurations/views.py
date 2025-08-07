from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from social_django.utils import load_strategy

from openlxp_authentication.models import SAMLConfiguration
from openlxp_authentication.serializers import SAMLConfigurationSerializer

from .models import CourseInformationMapping
from .serializers import CatalogsSerializer, CourseInformationMappingSerializer


class CatalogConfigurationView(APIView):
    """Catalog Configuration View"""

    def get(self, request):
        """Returns the XDSUI configuration fields from the model"""
        catalogs = request.user.catalogs.exclude(image='')
        serializer = CatalogsSerializer(catalogs, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class CourseInformationMappingView(APIView):
    """Course Information Mapping View"""

    def get(self, request):
        """Returns the CourseInformationMapping fields from the model"""
        mapping = CourseInformationMapping.objects.all().first()
        serializer = CourseInformationMappingSerializer(mapping)

        return Response(serializer.data, status.HTTP_200_OK)


class SSOConfigurationView(APIView):
    """SSO Configuration View"""

    def get(self, request):
        """Returns the SSO configurations"""

        login_path = load_strategy(request).build_absolute_uri('/')[:-1]

        serialized_ssos = [
            {"path": login_path + conf['endpoint'], "name": conf['name']}
            for conf in
            SAMLConfigurationSerializer(SAMLConfiguration.
                                        objects.all(), many=True
                                        ).data]

        return Response({"single_sign_on_options": serialized_ssos})