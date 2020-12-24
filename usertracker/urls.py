from django.contrib import admin
from django.urls import path
from .views import tracker_url

urlpatterns = [
    path('', tracker_url),
]
