# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.decorators import task
from django.conf import settings
from django.core.mail import send_mail
from .models import Reminder


@task
def send_reminder(pk):
    #Send Email Reminder at specified time.
    print ("Sending email.")
    notify = Reminder.objects.get(pk = pk)
    mail_to = [notify.email, ]
    subject = "Reminder"
    message = notify.message
    mail_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, mail_from, mail_to, fail_silently = False)

@task
def send_sms(pk):
    #Send SMS Reminder at specified time.
    print ("Sending SMS")
    notify = Reminder.objects.get(pk = pk)
    sms_to = notify.phone
    message = notify.message
    #sendSMS(sms_to, message)
