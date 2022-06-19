from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


@admin.register(Capability)
class CapabilityAdmin(ModelAdmin):
    list_display = ('__str__', 'type')
    readonly_fields = ('state', 'parameters',)
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

    # POST SAVE TRIGGER
    # ToDo: Костыль для m2m
    def save_related(self, request, form, formsets, change):
        # super(ModelAdmin, self).save_related(request, form, formsets, change)
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
        # end super()

        if form.instance.type == CapabilityType.MODE.value:
            form.instance.init_mode_post()
            form.instance.save()

@admin.register(CapabilityMode)
class CapabilityModeAdmin(ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(ModelAdmin):
    list_filter = (
        'author',
    )
