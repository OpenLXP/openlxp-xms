from core.models import XMSConfiguration
from rest_framework.test import APITestCase
from users.models import UserProfile


class TestSetUp(APITestCase):
    """Class with setup and teardown for tests in XIS"""

    def setUp(self):
        """Function to set up necessary data for testing"""

        self.su_username = "super@test.com"
        self.su_password = "1234"

        self.super_user = UserProfile.objects.create_superuser(
            self.su_username,
            self.su_password,
            first_name="super",
            last_name="user")

        self.xms_config = \
            XMSConfiguration(target_xis_metadata_api="www.test.com",
                             xis_catalogs_api="www.catalogs.com")
        self.xms_config.save()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
