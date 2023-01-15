from django.urls import path
from . import views

urlpatterns = [
    path("", views.sender_mail_function_view, name='sender'),
]