from django.contrib import admin

from core.models import XMSConfiguration, ReceiverEmailConfiguration, \
    SenderEmailConfiguration


# Register your models here.
@admin.register(XMSConfiguration)
class XMSConfigurationAdmin(admin.ModelAdmin):
    list_display = ('xis_host',)
    fields = [('xis_host',)]


@admin.register(ReceiverEmailConfiguration)
class ReceiverEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('email_address',)


@admin.register(SenderEmailConfiguration)
class SenderEmailConfigurationAdmin(admin.ModelAdmin):
    list_display = ('sender_email_address',)
