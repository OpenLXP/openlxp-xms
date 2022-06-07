from rest_framework import serializers

from configurations.models import CatalogConfigurations


# config serializers
class CatalogsSerializer(serializers.ModelSerializer):
    """Serializes the Catalogs Model"""
    image = serializers.CharField(source='image_path')

    class Meta:
        model = CatalogConfigurations

        fields = '__all__'
