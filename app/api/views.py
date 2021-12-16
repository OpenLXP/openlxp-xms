import logging

import requests
from requests.exceptions import HTTPError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from core.models import XMSConfiguration

logger = logging.getLogger('dict_config_logger')


class CatalogsView(APIView):
    """Catalog List View"""

    def get(self, request):
        """Handles listing all available catalogs"""
        errorMsg = {
            "message": "Error fetching catalogs please check the logs."
        }

        try:
            api_url = XMSConfiguration.objects.first()\
                .xis_catalogs_api

            # make API call
            response = requests.get(api_url)
            responseJSON = json.dumps(response.json())
            responseDict = json.loads(responseJSON)
            logger.info(responseJSON)

            if (response.status_code == 200):
                return Response(responseDict,
                                status.HTTP_200_OK)
            else:
                return Response(responseDict,
                                status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            errorMsg = {"message": "error reaching out to configured XIS API; "
                        + "please check the XIS logs"}
            logger.error(e)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)

        except HTTPError as http_err:
            logger.error(http_err)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListExperiencesView(APIView):
    """Experiences List View"""

    def get(self, request):
        """Handles listing requests for experiences"""
        errorMsg = {
            "message": "Error fetching experiences please check the logs."
        }

        try:
            metadata_xis_api = XMSConfiguration.objects.first()\
                .target_xis_metadata_api
            api_url = metadata_xis_api + '?' + request.META['QUERY_STRING']

            # make API call
            response = requests.get(api_url)
            responseJSON = json.dumps(response.json())
            responseDict = json.loads(responseJSON)
            logger.info(responseJSON)

            if (response.status_code == 200):
                return Response(responseDict,
                                status.HTTP_200_OK)
            else:
                return Response(responseDict,
                                status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            errorMsg = {"message": "error reaching out to configured XIS API; "
                        + "please check the XIS logs"}
            logger.error(e)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)

        except HTTPError as http_err:
            logger.error(http_err)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExperiencesView(APIView):
    """Experiences View"""

    def get(self, request, id):
        """Fetches the record of the corresponding course id"""
        return self._experience(request, id)

    def patch(self, request, id):
        """Modifies the record of the corresponding course id"""
        return self._experience(request, id)

    def _experience(self, request, id):
        """This method defines an API to fetch or modify the record of the
            corresponding course id"""
        errorMsg = {
            "message": "Error fetching experiences please check the logs."
        }

        try:
            metadata_xis_api = XMSConfiguration.objects.first()\
                .target_xis_metadata_api
            api_url = metadata_xis_api + id + '/'

            if request.method == 'GET':
                # make API call
                response = requests.get(api_url)
            elif request.method == 'PATCH':
                response = requests.patch(api_url, json=request.data)

            responseJSON = json.dumps(response.json())
            responseDict = json.loads(responseJSON)
            logger.info(responseJSON)

            if (response.status_code == 200):

                return Response(responseDict,
                                status.HTTP_200_OK)
            else:
                return Response(responseDict,
                                status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as e:
            errorMsg = {"message": "error reaching out to configured XIS API; "
                        + "please check the XIS logs"}
            logger.error(e)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)

        except HTTPError as http_err:
            logger.error(http_err)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)

            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
