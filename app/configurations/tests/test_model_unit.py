from configurations.models import XMSConfigurations
from django.forms import ValidationError
from django.test import TestCase, tag


@tag("xms_config_model")
class XMSConfigurationModelTests(TestCase):
    def test_creating_xms_default_config(self):
        """
        Test that the XMSConfigurations model can be created with default values.
        """
        XMSConfigurations.objects.create()
        # get the created object
        xms_config = XMSConfigurations.objects.first()

        self.assertEqual(
            xms_config.target_xis_metadata_host, "http://localhost:8080/api/metadata/"
        )
        self.assertEqual(
            xms_config.target_xis_catalogs_host, "http://localhost:8080/api/catalogs/"
        )

    def test_creating_xms_config_with_values(self):
        """
        Test that the XMSConfigurations model can be created with custom values.
        """
        XMSConfigurations.objects.create(
            target_xis_metadata_host="http://test:8080/api/metadata/",
            target_xis_catalogs_host="http://test:8080/api/catalogs/",
        )
        # get the created object
        xms_config = XMSConfigurations.objects.first()

        self.assertEqual(
            xms_config.target_xis_metadata_host, "http://test:8080/api/metadata/"
        )
        self.assertEqual(
            xms_config.target_xis_catalogs_host, "http://test:8080/api/catalogs/"
        )

    def test_creating_multiple_xms_config(self):
        """
        Test that a user cannot create multiple XMSConfigurations models.
        """
        XMSConfigurations.objects.create(
            target_xis_metadata_host="http://test:8080/api/metadata/",
            target_xis_catalogs_host="http://test:8080/api/catalogs/",
        )
        with self.assertRaises(ValidationError):
            # attempt to save another XMSConfigurations model
            XMSConfigurations.objects.create(
                target_xis_metadata_host="http://test:8080/api/metadata/",
                target_xis_catalogs_host="http://test:8080/api/catalogs/",
            )
