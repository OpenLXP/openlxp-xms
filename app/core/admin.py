from core.models import (
    ReceiverEmailConfiguration,
    SenderEmailConfiguration,
)
from django.contrib import admin


@admin.register(ReceiverEmailConfiguration)
class ReceiverEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ("email_address",)


@admin.register(SenderEmailConfiguration)
class SenderEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ("sender_email_address",)
