from django.test import SimpleTestCase, tag

from core.models import XMSConfiguration


@tag('unit')
class ModelTests(SimpleTestCase):

    def test_create_xms_configuration(self):
        """Test that creating a new XMS Configuration entry is successful
        with defaults """
        xis_host = "www.test.com"

        xmsConfig = XMSConfiguration(xis_host=xis_host)

        self.assertEqual(xmsConfig.xis_host, xis_host)
