from django.shortcuts import render, HttpResponse

# Create your views here.
def tracker_url(request):
    return HttpResponse("monkey")