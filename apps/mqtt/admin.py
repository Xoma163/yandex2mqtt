from django.contrib import admin

from .forms import MqttConfigForm
from .models import *


@admin.register(MqttConfig)
class MqttConfigAdmin(admin.ModelAdmin):
    form = MqttConfigForm
