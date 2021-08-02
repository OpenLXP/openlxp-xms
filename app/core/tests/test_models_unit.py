from unittest.mock import patch

from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from core.models import (ReceiverEmailConfiguration, SenderEmailConfiguration,
                         XMSConfiguration)


@tag('unit')
class ModelTests(TestCase):

    def test_create_xms_configuration(self):
        """Test that creating a new XMS Configuration entry is successful
        with defaults """
        xis_host = "www.test.com"
        catalog_api = "www.catalogs.com"

        xmsConfig = XMSConfiguration(target_xis_metadata_api=xis_host,
                                     xis_catalogs_api=catalog_api)

        self.assertEqual(xmsConfig.target_xis_metadata_api, xis_host)
        self.assertEqual(xmsConfig.xis_catalogs_api, catalog_api)

    def test_create_two_xms_configuration(self):
        """Test that trying to create more than one XMS Configuration object
            throws ValidationError """
        with self.assertRaises(ValidationError):
            xmsConfig = \
                XMSConfiguration(target_xis_metadata_api="www.test.com",
                                 xis_catalogs_api="www.catalogs.com")
            xmsConfig2 = \
                XMSConfiguration(target_xis_metadata_api="www.test.com",
                                 xis_catalogs_api="www.catalogs.com")
            xmsConfig.save()
            xmsConfig2.save()

    def test_create_receiver_config(self):
        """Test creating a receiver email configuration"""
        receiver_config = \
            ReceiverEmailConfiguration(email_address="test@email.com")

        with patch('core.models.email_verification') as email_verification:
            email_verification.return_value = email_verification
            receiver_config.save()

            self.assertTrue(receiver_config.pk is not None)

    def test_create_sender_config(self):
        """Test creating a sender email config"""
        sender_config = \
            SenderEmailConfiguration(sender_email_address="test@email.com")

        with patch('core.models.email_verification') as email_verification:
            email_verification.return_value = email_verification
            sender_config.save()

            self.assertTrue(sender_config.pk is not None)
