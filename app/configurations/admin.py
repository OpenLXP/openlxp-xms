from django.contrib import admin

from configurations.models import CatalogConfigurations, XMSConfigurations

# Register your models here.


@admin.register(XMSConfigurations)
class XMSConfigurationsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "target_xis_host",
        # "target_xis_catalogs_host",
    )
    # fields to display in the admin site
    fieldsets = (
        (
            "XIS Configuration",
            {
                # on the same line
                "fields": (
                    "target_xis_host",
                    # "target_xis_catalogs_host",
                )
            },
        ),
    )


@admin.register(CatalogConfigurations)
class CatalogsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    # fields to display in the admin site
    fieldsets = (
        (
            "Catalog Configuration",
            {
                # on the same line
                "fields": (
                    "name",
                    "image",
                )
            },
        ),
    )
