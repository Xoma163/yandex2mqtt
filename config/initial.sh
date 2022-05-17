#!/bin/bash
sudo apt install -y python3.8 python3.8-venv python3-venv python3.8-dev python3-wheel postgresql libpq-dev uwsgi
python3.8 -m venv venv
set -e
source ./venv/bin/activate
pip install wheel
pip install --upgrade pip setuptools wheel virtualenv
pip install -r requirements.txt

cp .env_example .env
secret_key=$(python manage.py shell --command="from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
sed -i "s/SECRET_KEY=/SECRET_KEY=$secret_key/g" .env
read -p "Enter database url (e.g. postgres://USERNAME:PASSWORD@localhost:5432/DBNAME):" database_url
sed -i "s#DATABASE_URL=postgres://USERNAME:PASSWORD@localhost:5432/DBNAME#DATABASE_URL=${database_url}#g" .env

old_project_name="DjangoTemplate"
read -p "Enter new project name: " new_project_name
mv $old_project_name $new_project_name

sed -i "s/$old_project_name/$new_project_name/g" $new_project_name/settings.py
sed -i "s/django.template.backends.django.${new_project_name}s/django.template.backends.django.${old_project_name}s/g" $new_project_name/settings.py
sed -i "s/$old_project_name/$new_project_name/g" $new_project_name/asgi.py
sed -i "s/$old_project_name/$new_project_name/g" $new_project_name/wsgi.py
sed -i "s/$old_project_name/$new_project_name/g" manage.py

python manage.py makemigrations
python manage.py migrate

echo "Create superuser for django-admin"
python manage.py createsuperuser

rm config/initial.sh
echo "" > README.md
git add .
git commit -m "Replace template for project ${new_project_name}"
git push

echo "done"