from django.http import HttpResponse
from django.urls import path
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! The current server time is {now}'.format(now=str(now)))

def hello(request):
    return HttpResponse("Oh, hi!")
