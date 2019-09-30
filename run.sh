#!/bin/bash

python3 /code/manage.py wait_for_db
python3 /code/manage.py migrate --noinput
python3 /code/manage.py collectstatic --noinput
python3 /code/manage.py runserver 0.0.0.0:8000
