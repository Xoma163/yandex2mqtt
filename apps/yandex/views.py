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

    devices = [device.get_json() for device in user.devices]

    data = {
        "request_id": request.headers['X-Request-Id'],
        "payload": {
            "user_id": str(user.pk),
            "devices": devices
        }
    }
    return UTF8JsonResponse(data, status=200)


@csrf_exempt
def user_devices_action(request):
    data = json.loads(request.body)['payload']
    return HttpResponse(status=200)


@csrf_exempt
def user_devices_query(request):
    return HttpResponse(status=200)


@csrf_exempt
def user_unlink(request):
    return HttpResponse(status=200)
