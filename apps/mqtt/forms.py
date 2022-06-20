from django import forms

from apps.mqtt.models import MqttConfig


class MqttConfigForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = MqttConfig
        widgets = {
            'password': forms.PasswordInput(),
        }
