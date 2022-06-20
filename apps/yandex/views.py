import json

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views import View
from apps.main.mixins import CSRFExemptMixin


class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        super().__init__(*args, json_dumps_params=json_dumps_params, **kwargs)


class IndexView(View):
    def head(self, request):
        return HttpResponse(status=200)


class UserDevicesView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponse(status=200)

        devices = request.user.devices.all()
        devices_data = [device.get_for_device_list() for device in devices]

        response_data = {
            "request_id": request.headers['X-Request-Id'],
            "payload": {
                "user_id": str(request.user.pk),
                "devices": devices_data
            }
        }

        return UTF8JsonResponse(response_data, status=200)


class UserDevicesActionView(CSRFExemptMixin, View):
    def post(self, request):
        # AccessToken.objects.get(token=request.headers['authorization'].replace("Bearer ",""))
        if request.user.is_anonymous:
            return HttpResponse(status=200)
        body = json.loads(request.body)
        devices = body['payload']['devices']
        devices_data = [request.user.devices.get(pk=device['id']).get_for_switch_state(device['capabilities']) for device in
                        devices]
        response_data = {
            "request_id": request.headers['X-Request-Id'],
            "payload": {
                "devices": devices_data
            }
        }
        return UTF8JsonResponse(response_data, status=200)


class UserDevicesQueryView(CSRFExemptMixin, View):
    def post(self, request):
        if request.user.is_anonymous:
            return HttpResponse(status=200)
        body = json.loads(request.body)
        devices_pk = [x['id'] for x in body['devices']]
        devices = request.user.devices.filter(pk__in=devices_pk)
        devices_data = [device.get_for_state() for device in devices]

        response_data = {
            "request_id": request.headers['X-Request-Id'],
            "payload": {
                "devices": devices_data
            }
        }

        return UTF8JsonResponse(response_data, status=200)


class UserUnlinkView(CSRFExemptMixin, View):
    def post(self, request):
        return HttpResponse(status=200)
