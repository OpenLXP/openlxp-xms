from django.urls import path

import configurations.views as views

# namespace
app_name = "configurations"

urlpatterns = [
     path("config/catalogs/", views.CatalogConfigurationView.as_view(),
         name="catalogs-config"),
     path("config/info-mapping/", views.CourseInformationMappingView.as_view(),
         name="course-information"),
     path("config/sso/", views.SSOConfigurationView.as_view(),
         name="sso-config")
    ]