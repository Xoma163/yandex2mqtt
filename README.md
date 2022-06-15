```
sudo ln -s "$PWD/config/systemd/yandex2mqtt.service" /etc/systemd/system/ 
sudo systemctl daemon-reload
```

```
sudo ln -s "$PWD/config/nginx/yandex2mqtt.config" /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```