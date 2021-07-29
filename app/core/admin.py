from django.contrib import admin

from core.models import (ReceiverEmailConfiguration, SenderEmailConfiguration,
                         XMSConfiguration)


# Register your models here.
@admin.register(XMSConfiguration)
class XMSConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'target_xis_metadata_api', 'xis_catalogs_api',)
    fields = [('target_xis_metadata_api', 'xis_catalogs_api',)]


@admin.register(ReceiverEmailConfiguration)
class ReceiverEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('email_address',)


@admin.register(SenderEmailConfiguration)
class SenderEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('sender_email_address',)
