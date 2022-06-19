from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view()),  # head
    path('/user/devices', UserDevicesView.as_view()),  # get
    path('/user/devices/action', UserDevicesActionView.as_view()),  # post
    path('/user/devices/query', UserDevicesQueryView.as_view()),  # post
    path('/user/unlink', UserUnlinkView.as_view()),  # post
]
