## Как установить проект

**Для работы проекта требуется ssl сертификат и доменное имя.**

### Автоматический режим

1. Заранее создать базу данных (postgres, например)
2. Конфигурируем под свои нужды `config/systemd/yandex2mqtt.service` и `config/nginx/yandex2mqtt.config`
3. `./install.sh`
4. В файле .env

### Ручной режим

```shell
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa # Для python3.8
sudo apt install -y python3.8 python3.8-venv python3-venv python3.8-dev python3-wheel postgresql libpq-dev uwsgi nginx

python3.8 -m venv venv # создаём venv
source ./venv/bin/activate # активируем venv
pip install wheel # устанавливаем wheel
pip install --upgrade pip setuptools virtualenv # обновляем pip setuptools virtualenv
pip install -r requirements.txt # устанавливаем зависимости

cp .env_example .env # копируем енвы
# заполняем DATABASE_URL, ALLOWED_HOSTS, SECRET_KEY

python manage.py migrate # делаем миграции

python manage.py createsuperuser # создаём суперюзера

sudo ln -s "$PWD/config/systemd/yandex2mqtt.service" /etc/systemd/system/ # создаём симлинк на сервис
sudo systemctl daemon-reload # перезагружаем

sudo ln -s "$PWD/config/nginx/yandex2mqtt.config" /etc/nginx/sites-enabled/ # создаём симлинк на конфиг nginx
sudo systemctl restart nginx # перезагружаем

sudo systemctl start yandex2mqtt # запуск проекта
```
