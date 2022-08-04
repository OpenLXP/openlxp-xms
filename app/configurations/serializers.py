from rest_framework import serializers

from .models import CatalogConfigurations


# config serializers
class CatalogsSerializer(serializers.ModelSerializer):
    """Serializes the Catalogs Model"""
    image = serializers.CharField(source='image_path')

    class Meta:
        model = CatalogConfigurations

        fields = ['name', 'image', ]
