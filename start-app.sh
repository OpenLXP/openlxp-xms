#!/usr/bin/env bash
cd /tmp/openlxp-xms/app
python manage.py waitdb 
python manage.py migrate 
python manage.py collectstatic --no-input
python manage.py loaddata admin_theme_data.json 
cd /tmp/
pwd 
./start-server.sh