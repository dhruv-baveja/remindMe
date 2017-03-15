from django.db import models

#Reminder Model.
class Reminder(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
