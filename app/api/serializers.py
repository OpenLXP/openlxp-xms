from rest_framework import serializers

from configurations.models import Catalogs


# config serializers
class CatalogsSerializer(serializers.ModelSerializer):
    """Serializes the Catalogs Model"""

    class Meta:
        model = Catalogs

        fields = '__all__'
