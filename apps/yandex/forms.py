from django import forms

from apps.yandex.consts import PropertyType, ALLOWED_UNITS_BY_FLOAT_INSTANCE, ALLOWED_EVENTS_BY_EVENT_INSTANCE, \
    CapabilityType, ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE


class BaseAbilityForm(forms.ModelForm):
    def get_display(self, field, value=None):
        if not value:
            value = self.cleaned_data[field]
        for choice in self.fields[field].choices:
            if choice[0] == value:
                return choice[1]

    def field_required(self, field):
        self.add_error(field, f"Это поле должно быть заполнено для типа \"{self.get_display('type')}\"")

    def field_required_one_of(self, field):
        self.add_error(field, f"Это поле или другие должны быть заполнено для типа \"{self.get_display('type')}\"")


class PropertyAdminForm(BaseAbilityForm, forms.ModelForm):
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        if cleaned_data['type'] == PropertyType.FLOAT.value:
            if not cleaned_data['float_instance']:
                self.field_required('float_instance')
                return cleaned_data
            if cleaned_data['unit']:
                if cleaned_data['unit'] not in ALLOWED_UNITS_BY_FLOAT_INSTANCE[cleaned_data['float_instance']]:
                    allowed_units_str = ", ".join([self.get_display('unit', x) for x in
                                                   ALLOWED_UNITS_BY_FLOAT_INSTANCE[cleaned_data['float_instance']]])
                    self.add_error("unit",
                                   f"Единица измерения для типа \"{self.get_display('type')}\" может принимать следующие значения: \"{allowed_units_str}\"")
                    return cleaned_data
        elif cleaned_data['type'] == PropertyType.EVENT.value:
            if not cleaned_data['event_instance'] or len(cleaned_data['events']) == 0:
                self.field_required('event_instance')
                self.field_required('events')
                return cleaned_data

            for event in cleaned_data['events']:
                if event not in ALLOWED_EVENTS_BY_EVENT_INSTANCE[cleaned_data['event_instance']]:
                    allowed_events_str = ", ".join([self.get_display('events', x) for x in
                                                    ALLOWED_EVENTS_BY_EVENT_INSTANCE[cleaned_data['event_instance']]])
                    self.add_error('events',
                                   f"Событие для типа \"{self.get_display('type')}\" может принимать следующие значения: \"{allowed_events_str}\" ")
                    return cleaned_data


class CapabilityAdminForm(BaseAbilityForm, forms.ModelForm):
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        if cleaned_data['type'] == CapabilityType.ON_OFF.value:
            pass
        elif cleaned_data['type'] == CapabilityType.COLOR_SETTING.value:
            if not cleaned_data['color_model'] and not cleaned_data['temp_k_min'] and not cleaned_data['temp_k_max']:
                self.field_required_one_of('color_model')
                self.field_required_one_of('temp_k_min')
                self.field_required_one_of('temp_k_max')

            if cleaned_data['temp_k_min'] and not cleaned_data['temp_k_max']:
                self.field_required('temp_k_max')
                return cleaned_data
            if cleaned_data['temp_k_max'] and not cleaned_data['temp_k_min']:
                self.field_required('temp_k_min')
                return cleaned_data
            if cleaned_data['temp_k_max'] and cleaned_data['temp_k_min']:
                if cleaned_data['temp_k_max'] < cleaned_data['temp_k_min']:
                    self.add_error('temp_k_min', "Это значение должно быть меньше максимального значения")
                    self.add_error('temp_k_max', "Это значение должно быть больше минимального значения")

        elif cleaned_data['type'] == CapabilityType.MODE.value:
            if not cleaned_data['mode_instance']:
                self.field_required('mode_instance')
            if len(cleaned_data['modes']) == 0:
                self.field_required('modes')
            return cleaned_data
        elif cleaned_data['type'] == CapabilityType.RANGE.value:
            if not cleaned_data['range_instance']:
                self.field_required('range_instance')
                return cleaned_data

            if cleaned_data['unit']:
                if cleaned_data['unit'] not in ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE[cleaned_data['range_instance']]:
                    allowed_events_str = ", ".join([self.get_display('unit', x) for x in
                                                    ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE[
                                                        cleaned_data['range_instance']]])
                    self.add_error('unit',
                                   f"Событие для типа \"{self.get_display('unit')}\" может принимать следующие значения: \"{allowed_events_str}\" ")
            if cleaned_data['range_min'] or cleaned_data['range_max'] or cleaned_data['range_precision']:
                if not cleaned_data['range_min']:
                    self.field_required('range_min')
                if not cleaned_data['range_max']:
                    self.field_required('range_max')
                if not cleaned_data['range_precision']:
                    self.field_required('range_precision')
                return cleaned_data
            if cleaned_data['range_min'] > cleaned_data['range_max']:
                self.add_error('range_min', "Это значение должно быть меньше максимального значения")
                self.add_error('range_max', "Это значение должно быть больше минимального значения")

        elif cleaned_data['type'] == CapabilityType.TOGGLE.value:
            if not cleaned_data['toggle_instance']:
                self.field_required('toggle_instance')
        elif cleaned_data['type'] == CapabilityType.VIDEO_STREAM.value:
            if not cleaned_data['protocol']:
                self.field_required('protocol')

        return cleaned_data
