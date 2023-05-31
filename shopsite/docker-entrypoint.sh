#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations script
echo "Apply database migrations script"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
# uwsgi --ini uwsgi.ini