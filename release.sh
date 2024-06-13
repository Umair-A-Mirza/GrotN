#!/bin/bash
set -e
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput