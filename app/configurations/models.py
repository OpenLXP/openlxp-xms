from django.db import models
from django.forms import ValidationError
from django.urls import reverse

# Create your models here.


class XMSConfigurations(models.Model):
    """Model for XMS Configuration"""

    class Meta:
        # change the name shown
        verbose_name = "XMS Connection"

    # the following fields are required for XMS to connect to XIS

    target_xis_host = models.CharField(
        help_text="Enter the XIS host to query data",
        max_length=200,
        default="http://openlxp-xis:8020/api/managed-data/catalogs",
    )

    def get_absolute_url(self):
        """
        URL for displaying individual model records.
        """
        return reverse("xms-configuration", args=[str(self.id)])

    def __str__(self) -> str:
        """
        String for representing the Model object.
        """
        return f"{self.id}"

    def save(self, *args, **kwargs):
        """
        Override the save method to check if the XMSConfigurations already
        exists. Notifies the user if the model already exists.
        """
        if not self.pk and XMSConfigurations.objects.exists():
            raise ValidationError("XMSConfigurations model already exists")
        return super(XMSConfigurations, self).save(*args, **kwargs)
