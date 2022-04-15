from unittest.mock import patch

from ddt import ddt
from django.test import tag
from django.urls import reverse
from rest_framework import status

from api.tests.test_setup import TestSetUp


@tag("unit")
@ddt
class XISViewsTests(TestSetUp):
    def test_xis_get_catalogs_view(self):
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
                response.data, ["catalog_1", "catalog_2"],
            )

    def test_xis_get_catalogs_view_error(self):
        """
        Tests the catalog api returns a error when the status code is not 200
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

    def test_xis_get_catalog_experiences_view(self):
        """
        Tests that the catalog api returns a list of experiences for a catalog
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
                "experiences": [
                    [
                        "experience_1",
                        "experience_2",
                    ]
                ],
            },
        )

    def test_xis_get_catalog_experiences_view_error_getting_catalogs(self):
        """
        Tests the catalog api returns a error when the status code returned
        from get xis catalogs is not 200
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

    def test_xis_get_catalog_experiences_view_error_provider_not_found(self):
        """
        Tests the catalog api returns an error when the provider is not a valid
        provider.
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

    def test_xis_get_catalog_experiences_view_error_getting_experiences(self):
        """
        Tests the catalog api returns an error when the status code returned is
        not 200
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

    def test_xis_get_experience_view(self):
        """
        Tests that the experience api returns the experience requested
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
        self.assertEqual(response.data, {"course": "title"})

    def test_xis_get_experience_error_getting_catalogs(self):
        """
        Test that the experience api returns an error when the status code is
        not 200
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

    def test_xis_get_experience_error_provider_not_found(self):
        """
        Tests that the experience api returns an error when the provider is not
        found in the list of available catalogs
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

    def test_xis_get_experience_error_getting_experience(self):
        """
        Tests that the experience api returns an error when there is an error
        getting the experience
        """

        self.client.login(username=self.su_username, password=self.su_password)
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

    def test_xis_post_experience_view(self):
        """
        Tests that the experience api writes and return the response for the
         experience requested
        """
        self.client.login(username=self.su_username, password=self.su_password)

        response = self.client.post(
            path=reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_1",
                    "experience_id": "experience_1",
                },
            ),
            data=self.post_experience_data_dict,
        )

        self.assertEqual(response.status_code, 201)

    def test_xis_post_experience_error_getting_catalogs(self):
        """
        Test that the experience api returns an error when the status code is
        not 200
        """
        self.client.login(username=self.su_username, password=self.su_password)

        self.mocked_get_xis_catalogs.return_value.status_code = 500

        response = self.client.post(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_1",
                    "experience_id": "experience_1",
                },
            ),
            data=self.post_experience_data_dict,
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "There was an error processing your request",
        )

    def test_xis_post_experience_error_provider_not_found(self):
        """
        Tests that the experience api returns an error when the provider is not
        found in the list of available catalogs
        """

        self.client.login(username=self.su_username, password=self.su_password)

        response = self.client.post(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_3",
                    "experience_id": "experience_1",
                },
            ),
            data=self.post_experience_data_dict,
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "The provider id does not exist in the XIS catalogs",
        )

    def test_xis_post_experience_error_getting_experience(self):
        """
        Tests that the experience api returns an error when there is an error
        getting the experience
        """

        self.client.login(username=self.su_username, password=self.su_password)
        self.mocked_get_xis_experience.return_value.status_code = 500

        response = self.client.post(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_2",
                    "experience_id": "experience_1",
                },
            ),
            data=self.post_experience_data_dict,
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "The experience does not exist in the XIS catalogs",
        )

    def test_xis_post_experience_error_posting_experience(self):
        """
        Tests that the experience api returns an error when there is an error
        getting the experience
        """

        self.client.login(username=self.su_username, password=self.su_password)
        self.mocked_post_xis_experience.return_value.status_code = 500

        response = self.client.post(
            reverse(
                "api:experience",
                kwargs={
                    "provider_id": "catalog_2",
                    "experience_id": "experience_1",
                },
            ),
            data=self.post_experience_data_dict,
        )

        # assert the response
        self.assertEqual(
            response.data["detail"],
            "There was an error processing your request",
        )
