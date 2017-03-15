from rest_framework import serializers
from reminder.models import Reminder

class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    #'title' field for displaying only message of the reminder.
    title = serializers.HyperlinkedIdentityField(view_name = 'reminder-title')

    class Meta:
        model = Reminder
        fields = ('id', 'url', 'email', 'phone', 'message', 'date', 'time', 'title',)
