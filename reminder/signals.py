from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_reminder
from .models import Reminder
from datetime import datetime
import pytz

@receiver(post_save, sender=Reminder)
def reminder_handler(sender, instance, **kwargs):
    if instance.email:
        dt = datetime.combine(instance.date, instance.time)
        time_zone = pytz.timezone('Asia/Kolkata')
        dt = time_zone.localize(dt)
        utcTime = dt.astimezone(pytz.utc)

        #send_reminder.apply_async(kwargs={'pk': instance.pk})
        send_reminder.apply_async(eta = utcTime,kwargs={'pk': instance.pk})
