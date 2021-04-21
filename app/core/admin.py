from django.contrib import admin

from core.models import XMSConfiguration


# Register your models here.
@admin.register(XMSConfiguration)
class XMSConfigurationAdmin(admin.ModelAdmin):
    list_display = ('xis_host',)
    fields = [('xis_host',)]
