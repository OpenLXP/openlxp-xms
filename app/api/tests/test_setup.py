from rest_framework.test import APITestCase

from core.models import XMSConfiguration


class TestSetUp(APITestCase):
    """Class with setup and teardown for tests in XIS"""

    def setUp(self):
        """Function to set up necessary data for testing"""
        self.xms_config = \
            XMSConfiguration(target_xis_metadata_api="www.test.com",
                             xis_catalogs_api="www.catalogs.com")
        self.xms_config.save()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
