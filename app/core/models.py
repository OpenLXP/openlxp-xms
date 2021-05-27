from django.db import models
from django.forms import ValidationError
from django.urls import reverse


class XMSConfiguration(models.Model):
    """Model for XMS Configuration """

    xis_host = models.CharField(
        help_text='Enter the host url for the XIS (Experience '
                  'Indexing Service)',
        max_length=200
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
