#!/usr/bin/env bash
# Exit the script if any command fails
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
