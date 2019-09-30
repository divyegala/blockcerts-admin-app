#!/bin/bash

python manage.py wait_for_db
python manage.py migrate --noinput
python manage.py seed
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
