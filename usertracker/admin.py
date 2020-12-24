from django.contrib import admin
from .models import Monitor

@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    fields = ('redirect', 'url_slug')
    list_display = ['redirect', 'full_url', 'activated', 'ip']
