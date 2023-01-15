from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery_django import settings


@shared_task(bind=True)
def send_mail_function(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'Hello from Celery django'
        message = "Lorem ipsum dolor at simet..."
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"