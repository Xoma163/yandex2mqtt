from django.db import models


# Create your models here.
class MqttConfig(models.Model):
    login = models.CharField("Логин", max_length=100, blank=True)
    password = models.CharField("Пароль", max_length=100, blank=True)
    url = models.CharField("URL", max_length=100, default="localhost")
    port = models.PositiveIntegerField("Порт", default=1883)

    def __str__(self):
        return f"{self.url}:{self.port}"

    class Meta:
        verbose_name = "Конфигурация MQTT"
        verbose_name_plural = "Конфигурации MQTT"