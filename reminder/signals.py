from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_reminder
from .models import Reminder
from datetime import datetime
from django.utils.dateparse import parse_date, parse_time, parse_datetime

@receiver(post_save, sender=Reminder)
def reminder_handler(sender, instance, **kwargs):
    if instance.email:
        send_reminder.apply_async(kwargs={'pk': instance.pk})
        #send_reminder.apply_async(eta = instance.date,kwargs={'pk': instance.pk})
