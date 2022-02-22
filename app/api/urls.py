from django.urls import include, path

from .views import XISAvailableCatalogs, XISCatalog, XISCatalogExperience

# namespace
app_name = "api"

urlpatterns = [
    path("catalogs/", XISAvailableCatalogs.as_view(), name="catalogs"),
    path(
        "catalogs/<str:provider_id>/",
        XISCatalog.as_view(),
        name="catalog-experiences",
    ),
    path(
        "catalogs/<str:provider_id>/<str:experience_id>/",
        XISCatalogExperience.as_view(),
        name="experience",
    ),
]
