# Generated by Django 3.1.14 on 2022-06-09 18:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configurations', '0003_auto_20220607_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogconfigurations',
            name='members',
            field=models.ManyToManyField(related_name='catalogs', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='catalogconfigurations',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
