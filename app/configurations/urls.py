from django.urls import path

import configurations.views as views

# namespace
app_name = "configurations"

urlpatterns = [
    path("config/catalogs/", views.CatalogConfigurationView.as_view(),
         name="catalogs-config"),
]
