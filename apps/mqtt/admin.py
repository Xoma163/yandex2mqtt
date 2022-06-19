from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(MqttConfig)
class MqttConfigAdmin(admin.ModelAdmin):
    pass
