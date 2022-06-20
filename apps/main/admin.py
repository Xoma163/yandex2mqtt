from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .forms import UserForm
from .models import *


# Register your models here.

@admin.register(User)
class UserAdmin(ModelAdmin):
    form = UserForm
