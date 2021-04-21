from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from core.models import XMSConfiguration


@tag('integration')
class ModelTests(TestCase):

    def test_create_two_xms_configuration(self):
        """Test that trying to create more than one XMS Configuration object
            throws ValidationError """
        with self.assertRaises(ValidationError):
            xmsConfig = XMSConfiguration(xis_host="www.test.com")
            xmsConfig2 = XMSConfiguration(xis_host="www.test-two.com")
            xmsConfig.save()
            xmsConfig2.save()
