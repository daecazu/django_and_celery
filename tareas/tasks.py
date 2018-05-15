from celery import Celery, shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from tutorialcelery import settings
@shared_task
def send_users_emails():
    subject = 'mensaje de prueba'
    message = ' Bienvenido esto es un mensaje de prueba Celery, rabbitmq y django'
    users = User.objects.all()
    for user in users:
        send_mail(subject,message,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)

    return '{} se envio el correo correctamente'.format(user.username)
