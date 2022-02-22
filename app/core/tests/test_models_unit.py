from unittest.mock import patch

from core.models import (
    ReceiverEmailConfiguration,
    SenderEmailConfiguration,
)
from django.core.exceptions import ValidationError
from django.test import TestCase, tag


@tag("unit")
class ModelTests(TestCase):

    def test_create_receiver_config(self):
        """Test creating a receiver email configuration"""
        receiver_config = ReceiverEmailConfiguration(email_address="test@email.com")

        with patch("core.models.email_verification") as email_verification:
            email_verification.return_value = email_verification
            receiver_config.save()

            self.assertTrue(receiver_config.pk is not None)

    def test_create_sender_config(self):
        """Test creating a sender email config"""
        sender_config = SenderEmailConfiguration(sender_email_address="test@email.com")

        with patch("core.models.email_verification") as email_verification:
            email_verification.return_value = email_verification
            sender_config.save()

            self.assertTrue(sender_config.pk is not None)
