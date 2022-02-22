from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.xis_helper_functions import (get_catalog_experiences,
                                            get_xis_catalogs,
                                            get_xis_experience)


class XISAvailableCatalogs(APIView):
    """Catalog List View"""

    def get(self, request):
        """Returns the list of catalogs found in the XIS"""

        # get the url for the XIS catalogs
        xis_catalogs_response = get_xis_catalogs()

        # check if the request was successful
        if xis_catalogs_response.status_code != 200:
            # return the error message
            return Response(
                {"detail": "There was an error processing your request."},
                status=xis_catalogs_response.status_code,
            )

        # return the response
        return Response(
            {"catalogs": xis_catalogs_response.json()}, status.HTTP_200_OK
        )


class XISCatalog(APIView):
    """Catalog View"""

    def get(self, request, provider_id):
        """Returns all the courses in the corresponding catalog

        Args:
            provider_id (string): the query parameter for the catalog
        """

        xis_catalogs_response = get_xis_catalogs()

        # check if the request was successful
        if xis_catalogs_response.status_code != 200:
            # return the error message
            return Response(
                {"detail": "There was an error processing your request"},
                status=xis_catalogs_response.status_code,
            )

        # validate that the provider_id is valid
        if provider_id not in xis_catalogs_response.json():
            return Response(
                {
                    "detail": "The provider id does not exist in the XIS catalogs"
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        provider_catalog_response = get_catalog_experiences(provider_id)

        # check if the request was successful
        if provider_catalog_response.status_code != 200:
            # return the error message
            return Response(
                {"detail": "There was an error processing your request"},
                status=provider_catalog_response.status_code,
            )

        catalog_experiences_list = provider_catalog_response.json()

        # given the maximum number of items per page
        # chunk the list into a list of lists of dictionaries
        catalog_experiences_chunks = [
            catalog_experiences_list[i : i + 10]
            for i in range(0, len(catalog_experiences_list), 10)
        ]

        return Response(
            {
                "total": len(catalog_experiences_list),
                "pages": len(catalog_experiences_chunks),
                "courses": catalog_experiences_chunks,
            },
            status=status.HTTP_200_OK,
        )


class XISCatalogExperience(APIView):
    """Experience from a specific catalog"""

    def get(self, request, provider_id, experience_id) -> Response:
        """Returns the experience from the corresponding catalog

        Args:
            provider_id (string): the query parameter for the catalog
            experience_id (string): the metadata_key_hash for the experience
        """

        xis_catalogs_response = get_xis_catalogs()

        # check if the request was successful
        if xis_catalogs_response.status_code != 200:
            # return the error message
            return Response(
                {"detail": "There was an error processing your request"},
                status=xis_catalogs_response.status_code,
            )

        # validate that the provider_id is valid
        if provider_id not in xis_catalogs_response.json():
            return Response(
                {
                    "detail": "The provider id does not exist in the XIS catalogs"
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        provider_experience_response = get_xis_experience(
            provider_id=provider_id, experience_id=experience_id
        )

        # check if the request was successful
        if provider_experience_response.status_code != 200:
            # return the error message
            return Response(
                {"detail": "There was an error processing your request"},
                status=provider_experience_response.status_code,
            )

        # grab the first experience returned in the response
        experience = provider_experience_response.json()[0]

        return Response({"experience": experience}, status=status.HTTP_200_OK)

    def post(self, request, provider_id, experience_id):
        """Returns the experience from the corresponding catalog

        Args:
            provider_id (string): the query parameter for the catalog
            experience_id (string): the metadata_key_hash for the experience
        """

        pass


# class ListExperiencesView(APIView):
#     """Experiences List View"""

#     def get(self, request):
#         """Handles listing requests for experiences"""
#         errorMsg = {"message": "Error fetching experiences please check the logs."}

#         try:
#             metadata_xis_api = XMSConfiguration.objects.first().target_xis_metadata_api
#             api_url = metadata_xis_api + "?" + request.META["QUERY_STRING"]

#             # make API call
#             response = requests.get(api_url)
#             responseJSON = json.dumps(response.json())
#             responseDict = json.loads(responseJSON)
#             logger.info(responseJSON)

#             if response.status_code == 200:
#                 return Response(responseDict, status.HTTP_200_OK)
#             else:
#                 return Response(responseDict, status.HTTP_503_SERVICE_UNAVAILABLE)
#         except requests.exceptions.RequestException as e:
#             errorMsg = {
#                 "message": "error reaching out to configured XIS API; "
#                 + "please check the XIS logs"
#             }
#             logger.error(e)

#             return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)

#         except Exception as err:
#             logger.error(err)

#             return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)


# class ExperiencesView(APIView):
#     """Experiences View"""

#     def get(self, request, id):
#         """Fetches the record of the corresponding course id"""
#         return self._experience(request, id)

#     def patch(self, request, id):
#         """Modifies the record of the corresponding course id"""
#         return self._experience(request, id)

#     def _experience(self, request, id):
#         """This method defines an API to fetch or modify the record of the
#         corresponding course id"""
#         errorMsg = {"message": "Error fetching experiences please check the logs."}

#         try:
#             metadata_xis_api = XMSConfiguration.objects.first().target_xis_metadata_api
#             api_url = metadata_xis_api + id + "/"

#             if request.method == "GET":
#                 # make API call
#                 response = requests.get(api_url)
#             elif request.method == "PATCH":
#                 response = requests.patch(api_url, json=request.data)

#             responseJSON = json.dumps(response.json())
#             responseDict = json.loads(responseJSON)
#             logger.info(responseJSON)

#             if response.status_code == 200:

#                 return Response(responseDict, status.HTTP_200_OK)
#             else:
#                 return Response(responseDict, status.HTTP_503_SERVICE_UNAVAILABLE)
#         except requests.exceptions.RequestException as e:
#             errorMsg = {
#                 "message": "error reaching out to configured XIS API; "
#                 + "please check the XIS logs"
#             }
#             logger.error(e)

#             return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)

#         except Exception as err:
#             logger.error(err)

#             return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
