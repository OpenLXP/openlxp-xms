from core.management.utils.notification import email_verification
from django.db import models
from django.forms import ValidationError
from django.urls import reverse


class XMSConfiguration(models.Model):
    """Model for XMS Configuration """

    target_xis_metadata_api = models.CharField(
        help_text='Enter the XIS api endpoint to query metadata',
        max_length=200,
        default='http://localhost:8080/api/metadata/'
    )
    xis_catalogs_api = models.CharField(
        help_text='Enter the XIS api endpoint to get catalogs',
        max_length=200,
        default='http://localhost:8080/api/catalogs/'
    )

    def get_absolute_url(self):
        """ URL for displaying individual model records."""
        return reverse('xms-configuration', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if not self.pk and XMSConfiguration.objects.exists():
            raise ValidationError('XMSConfiguration model already exists')
        return super(XMSConfiguration, self).save(*args, **kwargs)


class ReceiverEmailConfiguration(models.Model):
    """Model for Email Configuration """

    email_address = models.EmailField(
        max_length=254,
        help_text='Enter email personas addresses to send log data',
        unique=True)

    def get_absolute_url(self):
        """ URL for displaying individual model records."""
        return reverse('Configuration-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}'

    def save(self, *args, **kwargs):
        email_verification(self.email_address)
        return super(ReceiverEmailConfiguration, self).save(*args, **kwargs)


class SenderEmailConfiguration(models.Model):
    """Model for Email Configuration """

    sender_email_address = models.EmailField(
        max_length=254,
        help_text='Enter sender email address to send log data from')

    def save(self, *args, **kwargs):
        if not self.pk and SenderEmailConfiguration.objects.exists():
            raise ValidationError('There can only be one '
                                  'SenderEmailConfiguration instance')
        return super(SenderEmailConfiguration, self).save(*args, **kwargs)
