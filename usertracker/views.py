from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Monitor

def tracker_url(request, slug):
    m = get_object_or_404(Monitor, url_slug=slug)

    m.activated = True
    m.ip = get_client_ip(request)
    m.save()

    return redirect(m.redirect)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip