from django.urls import path

from .views import *

urlpatterns = [
    path('', index),  # head
    path('user/devices', user_devices),  # get
    path('user/devices/action', user_devices_action),  # post
    path('user/devices/query', user_devices_query),  # post
    path('user/unlink', user_unlink),  # post
]
