# Generated by Django 3.2.9 on 2022-02-01 13:00
import logging

from django.contrib.auth.management import create_permissions
from django.contrib.contenttypes.management import create_contenttypes
from django.db import migrations

GROUPS = ['System Operator', 'Experience Owner', 'Experience Manager',
          'Experience Facilitator', 'Experience Participant']
MODELS = ['catalogs', 'list experiences', 'experiences']
PERMISSIONS = ['view', 'add', 'change', 'delete']


def forwards_func(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Perm = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    for custom in MODELS:
        ct = ContentType.objects.filter(
            model=custom.replace(" ", "")
        )
        if ct.exists():
            ct.delete()

    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_contenttypes(app_config, verbosity=0)
        app_config.models_module = None

    for custom in MODELS:
        ContentType.objects.get_or_create(
            app_label='api',
            model=custom.replace(" ", "")
        )

    for group in GROUPS:
        new_group, created = Group.objects.get_or_create(name=group)

        for model in MODELS:
            for permission in PERMISSIONS:
                name = 'Can {} {}'.format(permission, model)
                print("Creating {}".format(name))

                model_comb = model
                value = model_comb.replace(" ", "")
                codename = '{}_{}'.format(permission, value)

                try:
                    content_type = \
                        ContentType.objects.get(model=value)
                    model_add_perm, created = \
                        Perm.objects.get_or_create(codename=codename,
                                                   name=name,
                                                   content_type=
                                                   content_type)
                except Perm.DoesNotExist:
                    logging.warning("Permission not found with name '{}'.".
                                    format(name))
                    continue

                new_group.permissions.add(model_add_perm)

    print("Moved permissions to api app.")


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=GROUPS
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_groups'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]