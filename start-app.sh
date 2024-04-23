#!/usr/bin/env bash

python manage.py waitdb 
python manage.py migrate 
python manage.py loaddata admin_theme_data.json 
cd /tmp/app/ 
pwd 
./start-server.sh