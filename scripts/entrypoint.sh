#!/bin/sh

cd /usr/src/app
python3 manage.py migrate
python3 manage.py collectstatic --noinput

gunicorn config.wsgi:application --bind 0.0.0.0:$PORT