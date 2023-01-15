from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_mail_function
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


# Create your views here.
def sender_mail_function_view(request):
    send_mail_function.delay()
    return HttpResponse("Send!")


def sender_mail_at_particular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=13, minute=9)
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name="schedule_mail_task_" + "1", # '1' should be unique
        task="sender.tasks.send_mail_function",
        # args=json.dumps([[2, 3]]) # To add some args.
    )
    return HttpResponse("Send & Done!")
