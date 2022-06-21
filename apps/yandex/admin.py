from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .forms import PropertyAdminForm, CapabilityAdminForm
from .models import *


class BaseAbilityModelAdmin(ModelAdmin):
    list_display = ('__str__', 'type')
    readonly_fields = ('parameters',)
    list_filter = ('device__author', 'device__yd', 'device__room', 'device', 'type')
    search_fields = ('name',)


@admin.register(Capability)
class CapabilityAdmin(BaseAbilityModelAdmin, ModelAdmin):
    fieldsets = (
        ('Общее', {
            'fields': ('name', 'type', 'device', 'retrievable', 'reportable', 'state', 'parameters'),
        }),
        ('mqtt', {
            'fields': ('mqtt_config', 'command_topic', 'state_topic', 'state_topic_retriever'),
        }),
        ('ColorSetting', {
            'fields': ('color_model', 'temp_k_min', 'temp_k_max'),
        }),
        ('Mode', {
            'fields': ('mode_instance', 'modes'),
        }),
        ('OnOff', {
            'fields': ('split',),
        }),
        ('Range', {
            'fields': ('range_instance', 'unit', 'random_access', 'range_min', 'range_max', 'range_precision'),
        }),
        ('Toggle', {
            'fields': ('toggle_instance',),
        }),
        ('VideoStream', {
            'fields': ('protocol',),
        })
    )
    form = CapabilityAdminForm


@admin.register(Property)
class PropertyAdmin(BaseAbilityModelAdmin, ModelAdmin):
    fieldsets = (
        ('Общее', {
            'fields': ('name', 'type', 'device', 'retrievable', 'reportable', 'state', 'parameters'),
        }),
        ('mqtt', {
            'fields': ('mqtt_config', 'state_topic', 'state_topic_retriever'),
        }),
        ('Float', {
            'fields': ('float_instance', 'unit'),
        }),
        ('Event', {
            'fields': ('event_instance', 'events'),
        })
    )
    form = PropertyAdminForm


@admin.register(YandexDialog)
class YandexDialogModeAdmin(ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(ModelAdmin):
    list_filter = ('author', 'yd', 'room', 'type')
