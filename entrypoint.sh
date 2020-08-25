#!/bin/sh
python3 /usr/src/app/manage.py migrate
python3 /usr/src/app/manage.py collectstatic --noinput --clear
python3 /usr/src/app/manage.py runserver 0.0.0.0:8000
