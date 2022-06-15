from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return HttpResponse(status=200)


@csrf_exempt
def user_devices(request):
    return HttpResponse(status=200)


@csrf_exempt
def user_devices_action(request):
    return HttpResponse(status=200)


@csrf_exempt
def user_devices_query(request):
    return HttpResponse(status=200)


@csrf_exempt
def user_unlink(request):
    return HttpResponse(status=200)
