from django.urls import path
from . import views

urlpatterns = [
    path("", views.sender_mail_function_view, name='sender'),
    path("scheduler/", views.sender_mail_at_particular_time, name='sender-schedule'),
]