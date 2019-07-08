from django.contrib import messages
from djangoapp.tasks.demo import *
from django.http import HttpResponse

def send_message(req):
    for i in range(100):
        add.delay(5,4)
    return HttpResponse('<h1>OK</h1>')