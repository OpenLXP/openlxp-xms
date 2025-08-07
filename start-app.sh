#!/usr/bin/env bash

python manage.py waitdb 
python manage.py migrate --skip-checks
python manage.py createcachetable 
python manage.py loaddata admin_theme_data.json 
python manage.py collectstatic --no-input 
cd /opt/app/ 
pwd 
./start-server.sh
