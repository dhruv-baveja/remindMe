from django.shortcuts import render

from reminder.models import Reminder
from reminder.serializers import ReminderSerializer
from rest_framework import viewsets,renderers
from rest_framework.response import Response

# Create your views here.

from rest_framework.decorators import detail_route

#Reminder viewset that provides provides `list`, `create`, `retrieve`,`update` and `destroy` actions.
class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    #Additional 'title' action for displaying only message of the reminder.
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def title(self, request, *args, **kwargs):
        reminder = self.get_object()
        return Response(reminder.message)
