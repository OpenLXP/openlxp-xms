import requests
from configurations.models import XMSConfigurations
from rest_framework import status
from rest_framework.response import Response


# helper function to get the catalogs from XIS
def get_xis_catalogs():
    """Get all the catalogs available in the XIS

    Returns:
        requests.Response: [dictionary]
    """

    # get the XMS configuration for the XIS catalog host
    xis_catalogs_url = (
        XMSConfigurations.objects.first().target_xis_catalogs_host
    )

    # request the catalogs from the XIS
    return requests.get(xis_catalogs_url)


# helper function to get an experience from XIS
def get_xis_experience(provider_id, experience_id):
    """
    Get a specific experience from a specific catalog

    Args:
        provider_id (string): the query parameter for the catalog
        experience_id (strint): the metadata_key_hash for the experience

    Returns:
        list: [dictionary]
    """

    xis_metadata_experience_url = (
        XMSConfigurations.objects.first().target_xis_metadata_host
    )

    xis_metadata_experience_url = (
        xis_metadata_experience_url
        + f"?provider_id={provider_id}&metadata_key_hash_list={experience_id}"
    )

    return requests.get(xis_metadata_experience_url)


# helper function to get all experiences from a catalog in XIS
def get_catalog_experiences(provider_id):
    """Get all the experiences for a given catalog

    Args:
        provider_id (string): the query parameter for the catalog

    Returns:
        list: [dictionary]
    """
    xis_metadata_url = (
        XMSConfigurations.objects.first().target_xis_metadata_host
    )
    xis_metadata_url = xis_metadata_url + f"?provider={provider_id}"

    # request the experiences from the specified catalog
    return requests.get(xis_metadata_url)
