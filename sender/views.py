from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_mail_function


# Create your views here.
def sender_mail_function_view(request):
    send_mail_function.delay()
    return HttpResponse("Send!")
