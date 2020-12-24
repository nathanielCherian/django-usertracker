from django.contrib import admin
from .models import Monitor

@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    fields = ('redirect', 'is_url', 'url_slug')
    list_display = ['full_url', 'redirect', 'activated', 'ip']
