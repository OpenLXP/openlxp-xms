import json
from unittest.mock import patch
from urllib import response

from api.tests.test_setup import TestSetUp
from configurations.models import XMSConfigurations
from ddt import ddt
from django.test import TestCase, tag
from django.urls import reverse
from requests.exceptions import HTTPError
from rest_framework import status


@tag("xis_views")
@ddt
class XISViewsTests(TestSetUp):
    def test_xis_catalogs_view(self):
        """
        Tests that the catalog api returns a list of catalogs
        """

        # mock the response from the get_xis_catalogs function
        with patch("api.views.get_xis_catalogs") as mocked_get:
            mocked_get.return_value.json.return_value = [
                "catalog_1",
                "catalog_2",
            ]
            mocked_get.return_value.status_code = 200

            # call the function
            response = self.client.get(reverse("api:catalogs"))

            # assert the response
            self.assertEqual(
                response.data, {"catalogs": ["catalog_1", "catalog_2"]}
            )

    def test_xis_catalogs_view_error(self):
        """
        Tests
        """
        with patch("api.views.get_xis_catalogs") as mocked_get:
            mocked_get.return_value.status_code = 500

            response = self.client.get(reverse("api:catalogs"))

            # assert the response
            self.assertEqual(
                response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            self.assertEqual(
                response.data["detail"],
                "There was an error processing your request.",
            )

    def test_xis_catalog_experiences_view(self):
        """
        Tests
        """
        self.client.login(username=self.su_username, password=self.su_password)
        # call the function
        response = self.client.get(
            reverse(
                "api:catalog-experiences",
                kwargs={"provider_id": "catalog_1"},
            )
        )

        # assert the response
        self.assertEqual(
            response.data,
            {
                "total": 2,
                "pages": 1,
                "courses": [
                    [
                        "experience_1",
                        "experience_2",
                    ]
                ],
            },
        )

    def test_xis_catalog_experiences_view_error_getting_catalogs(self):
        """
        Tests
        """
        self.client.login(username=self.su_username, password=self.su_password)
        self.mocked_get_xis_catalogs.return_value.status_code = 500
        # call the function
        response = self.client.get(
            reverse(
                "api:catalog-experiences",
                kwargs={"provider_id": "catalog_1"},
            )
        )
        # assert the response  returns a 500
        self.assertEqual(
            response.data["detail"],
            "There was an error processing your request",
        )

    def test_xis_catalog_experiences_view_error_provider_not_found(self):
        """
        Tests
        """
        self.client.login(username=self.su_username, password=self.su_password)
        # call the function
        response = self.client.get(
            reverse(
                "api:catalog-experiences",
                kwargs={"provider_id": "catalog_3"},
            )
        )
        # assert the response  returns a 500
        self.assertEqual(
            response.data["detail"],
            "The provider id does not exist in the XIS catalogs",
        )

    def test_xis_catalog_experiences_view_error_getting_experiences(self):
        """
        Tests
        """
        self.client.login(username=self.su_username, password=self.su_password)
        self.mocked_get_xis_experiences.return_value.status_code = 500
        # call the function
        response = self.client.get(
            reverse(
                "api:catalog-experiences",
                kwargs={"provider_id": "catalog_2"},
            )
        )
        # assert the response  returns a 500
        self.assertEqual(
            response.data["detail"],
            "There was an error processing your request",
        )

    def test_xis_experience_view(self):
        """
        Tests
        """
        self.client.login(username=self.su_username, password=self.su_password)

        response = self.client.get(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_1",
                    "experience_id": "experience_1",
                },
            ),
        )

        # assert the response
        self.assertEqual(response.data, {"experience": {"course": "title"}})

    def test_xis_experience_error_getting_catalogs(self):
        """
        Test
        """
        self.client.login(username=self.su_username, password=self.su_password)

        self.mocked_get_xis_catalogs.return_value.status_code = 500

        response = self.client.get(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_1",
                    "experience_id": "experience_1",
                },
            ),
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "There was an error processing your request",
        )

    def test_xis_experience_error_provider_not_found(self):
        """
        Tests
        """

        self.client.login(username=self.su_username, password=self.su_password)

        response = self.client.get(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_3",
                    "experience_id": "experience_1",
                },
            ),
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "The provider id does not exist in the XIS catalogs",
        )

    def test_xis_experience_error_getting_experience(self):
        """
        Tests
        """

        self.client.login(username=self.su_username, password=self.su_password)
        self.mocked_get_xis_experiences.return_value.status_code = 200
        self.mocked_get_xis_catalogs.return_value.status_code = 200
        self.mocked_get_xis_experience.return_value.status_code = 500

        response = self.client.get(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_2",
                    "experience_id": "experience_1",
                },
            ),
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "There was an error processing your request",
        )

    def test_xis_experience_error_getting_experience(self):
        """
        Test
        """
        pass
