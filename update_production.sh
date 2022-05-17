#!/bin/bash
git checkout master
git reset HEAD --hard
git clean -fd
git pull

#npm run build

venv/bin/python -m pip install --upgrade pip setuptools wheel
venv/bin/pip install -r requirements.txt
venv/bin/python manage.py migrate
venv/bin/python manage.py collectstatic --noinput

#sudo systemctl restart service_name
