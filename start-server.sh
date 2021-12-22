#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd openlxp-xms; python manage.py createsuperuser --no-input)
fi
(cd openlxp-xms; gunicorn openlxp_xms_project.wsgi --reload --user www-data --bind unix:/opt/xms.sock --workers 3) &
nginx -g "daemon off;"