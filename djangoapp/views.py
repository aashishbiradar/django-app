from django.contrib import messages
from tasks.demo import *

def send_message():
    add.delay(5,4)
    return '<h1>OK</h1>'