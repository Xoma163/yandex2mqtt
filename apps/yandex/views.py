import json

from django.http import HttpResponse
from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken


class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        super().__init__(*args, json_dumps_params=json_dumps_params, **kwargs)


@csrf_exempt
def index(request):
    return HttpResponse(status=200)


def user_devices(request):
    token = request.headers['authorization'].replace("Bearer ", "")
    user = AccessToken.objects.get(token=token).user

    devices = user.devices.all()
    devices_data = [device.get_for_device_list() for device in devices]

    response_data = {
        "request_id": request.headers['X-Request-Id'],
        "payload": {
            "user_id": str(user.pk),
            "devices": devices_data
        }
    }
    # response_data['payload']['devices'][0]['capabilities']
    return UTF8JsonResponse(response_data, status=200)


@csrf_exempt
def user_devices_action(request):
    token = request.headers['authorization'].replace("Bearer ", "")
    user = AccessToken.objects.get(token=token).user
    body = json.loads(request.body)
    devices = body['payload']['devices']
    devices_data = [user.devices.get(pk=device['id']).get_for_switch_state(device['capabilities']) for device in devices]
    response_data = {
        "request_id": request.headers['X-Request-Id'],
        "payload": {
            "devices": devices_data
        }
    }
    return UTF8JsonResponse(response_data, status=200)


@csrf_exempt
def user_devices_query(request):
    token = request.headers['authorization'].replace("Bearer ", "")
    user = AccessToken.objects.get(token=token).user
    body = json.loads(request.body)
    devices_pk = [x['id'] for x in body['devices']]
    devices = user.devices.filter(pk__in=devices_pk)
    devices_data = [device.get_for_state() for device in devices]

    response_data = {
        "request_id": request.headers['X-Request-Id'],
        "payload": {
            "devices": devices_data
        }
    }

    return UTF8JsonResponse(response_data, status=200)


@csrf_exempt
def user_unlink(request):
    return HttpResponse(status=200)
