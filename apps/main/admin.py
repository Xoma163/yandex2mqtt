from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(ModelAdmin):
    pass
