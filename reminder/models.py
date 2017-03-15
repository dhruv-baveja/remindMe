from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from datetime import datetime

#Reminder Model.
class Reminder(models.Model):
    email = models.EmailField(blank = True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length = 15, validators=[phone_regex], blank = True)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def clean(self):
        if not self.email and not self.phone:
            raise ValidationError(_('Either email or Phone is required.'))

        if datetime.combine(self.date, self.time) < datetime.now():
            raise ValidationError(_('Time can not be in past.'))
