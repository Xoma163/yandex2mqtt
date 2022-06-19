from django.contrib import admin
from .models import *


@admin.register(Capability)
class CapabilityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type')
    readonly_fields = ('state','parameters',)
    fieldsets = (
        ('Общее', {
            'fields': ('name', 'type', 'retrievable', 'reportable', 'state', 'parameters'),
        }),
        ('mqtt', {
            'fields': ('mqtt_config', 'command_topic', 'state_topic'),
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


@admin.register(CapabilityMode)
class CapabilityModeAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_filter = (
        'author',
    )
