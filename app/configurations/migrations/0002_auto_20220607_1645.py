# Generated by Django 3.1.14 on 2022-06-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the catalog', max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Catalog',
            },
        ),
        migrations.AlterField(
            model_name='xmsconfigurations',
            name='target_xis_host',
            field=models.CharField(default='http://openlxp-xis:8020/api/managed-data/catalogs', help_text='Enter the XIS host to query data', max_length=200),
        ),
    ]