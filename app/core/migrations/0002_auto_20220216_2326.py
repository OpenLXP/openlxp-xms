# Generated by Django 3.1.14 on 2022-02-16 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xmsconfiguration',
            name='target_xse_host',
            field=models.CharField(default='http://localhost:9200', help_text='Enter the XSE host to query', max_length=200),
        ),
        migrations.AddField(
            model_name='xmsconfiguration',
            name='xse_index',
            field=models.CharField(default='metadata_v1', help_text='Enter the metadata index to query', max_length=200),
        ),
    ]