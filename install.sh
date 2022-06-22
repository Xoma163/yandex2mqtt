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

python manage.py makemigrations
python manage.py migrate

echo "Create superuser for django-admin"
python manage.py createsuperuser