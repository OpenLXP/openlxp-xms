from django.urls import path

from .views import (CatalogConfigurationView, XISAvailableCatalogs, XISCatalog,
                    XISExperience)

# namespace
app_name = "api"

urlpatterns = [
    path("catalogs/", XISAvailableCatalogs.as_view(), name="catalogs"),
    path("config/catalogs/", CatalogConfigurationView.as_view(),
         name="catalogs-config"),
    path('catalogs/<str:provider_id>', XISCatalog.as_view(),
         name='catalog-experiences'),
    path("catalogs/<str:provider_id>/<str:experience_id>",
         XISExperience.as_view(), name="experience"),
]
