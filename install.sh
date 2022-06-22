sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt install -y python3.8 python3.8-venv python3-venv python3.8-dev python3-wheel postgresql libpq-dev uwsgi nginx

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

python manage.py migrate

echo "Create superuser for django-admin"
python manage.py createsuperuser

sudo ln -s "$PWD/config/systemd/yandex2mqtt.service" /etc/systemd/system/
sudo systemctl daemon-reload

sudo ln -s "$PWD/config/nginx/yandex2mqtt.config" /etc/nginx/sites-enabled/
sudo systemctl restart nginx