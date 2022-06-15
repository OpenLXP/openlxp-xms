from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CatalogConfigurations
from .serializers import CatalogsSerializer


class CatalogConfigurationView(APIView):
    """Catalog Configuration View"""

    def get(self, request):
        """Returns the XDSUI configuration fields from the model"""
        catalogs = CatalogConfigurations.objects.exclude(image='')
        serializer = CatalogsSerializer(catalogs, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
