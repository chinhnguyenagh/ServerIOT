from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db.models import base

# Register your models here.
from .models import *

class DevideAdminInline(admin.StackedInline):
    model = Device
    verbose_name = 'Devide'
    verbose_name_plural = 'Devides'

class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'temperature', 'humid','distance_door', 'distance_private_room']
    inlines = [DevideAdminInline]

admin.site.register(Home,HomeAdmin)
admin.site.register(Type)
admin.site.register(Esp)

