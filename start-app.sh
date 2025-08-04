#!/usr/bin/env bash

python manage.py waitdb 
python manage.py migrate 
python manage.py createcachetable 
python manage.py collectstatic --no-input 
python manage.py loaddata admin_theme_data.json 
cd /opt/app/ 
pwd 
./start-server.sh
