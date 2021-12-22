import json
from unittest.mock import patch

from ddt import ddt
from django.test import tag
from django.urls import reverse
from requests.exceptions import HTTPError
from rest_framework import status

from .test_setup import TestSetUp


@tag('unit')
@ddt
class ViewTests(TestSetUp):

    def test_get_catalogs(self):
        """Test that calling the endpoint /api/catalogs returns a list of
            catalogs"""
        url = reverse('api:catalogs')

        with patch('api.views.requests') as requests:
            http_resp = requests.return_value
            requests.get.return_value = http_resp
            http_resp.json.return_value = [{
                "test": "value"
            }]
            http_resp.status_code = 200

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_catalogs_error(self):
        """Test that calling the endpoint /api/catalogs returns an
            http error if an exception a thrown while reaching out to XIS"""
        url = reverse('api:catalogs')
        errorMsg = "error reaching out to configured XIS API; " + \
                   "please check the XIS logs"

        with patch('api.views.requests.get') as get_request:
            get_request.side_effect = [HTTPError]

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(responseDict['message'], errorMsg)

    def test_get_experiences(self):
        """Test that calling /api/experiences returns a list of
            experiences"""
        url = reverse('api:experiences')

        with patch('api.views.requests') as requests:
            http_resp = requests.return_value
            requests.get.return_value = http_resp
            http_resp.json.return_value = [{
                "test": "value"
            }]
            http_resp.status_code = 200

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_experiences_error(self):
        """Test that calling /api/experiences returns an error if the call
            to the XIS throws an http error"""
        url = reverse('api:experiences')
        errorMsg = "error reaching out to configured XIS API; " + \
                   "please check the XIS logs"

        with patch('api.views.requests.get') as get_request:
            get_request.side_effect = [HTTPError]

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(responseDict['message'], errorMsg)

    def test_get_experience(self):
        """Test that calling /api/experience/id returns an experience"""
        doc_id = '123456'
        url = reverse('api:experience', args=(doc_id,))

        with patch('api.views.requests') as requests:
            http_resp = requests.return_value
            requests.get.return_value = http_resp
            http_resp.json.return_value = {
                "test": "value"
            }
            http_resp.status_code = 200

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_experience_error(self):
        """Test that calling /api/experience/id returns an error if the call
            to the XIS throws an http error"""
        doc_id = '123456'
        url = reverse('api:experience', args=(doc_id,))
        errorMsg = "error reaching out to configured XIS API; " + \
                   "please check the XIS logs"

        with patch('api.views.requests.get') as get_request:
            get_request.side_effect = [HTTPError]

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.get(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(responseDict['message'], errorMsg)

    def test_patch_experience(self):
        """Test that calling /api/experience/id updates an experience"""
        doc_id = '123456'
        url = reverse('api:experience', args=(doc_id,))

        with patch('api.views.requests') as requests:
            http_resp = requests.return_value
            requests.patch.return_value = http_resp
            http_resp.json.return_value = {
                "test": "value"
            }
            http_resp.status_code = 200

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.patch(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_experience_error(self):
        """Test that calling /api/experience/id returns an error if the call
            to the XIS throws an http error"""
        doc_id = '123456'
        url = reverse('api:experience', args=(doc_id,))
        errorMsg = "error reaching out to configured XIS API; " + \
                   "please check the XIS logs"

        with patch('api.views.requests.patch') as patch_request:
            patch_request.side_effect = [HTTPError]

            self.client.login(username=self.su_username,
                              password=self.su_password)

            response = self.client.patch(url)
            responseDict = json.loads(response.content)

            self.assertEqual(response.status_code,
                             status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(responseDict['message'], errorMsg)
