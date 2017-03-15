from django.test import TestCase, override_settings

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
# Create your tests here.
from django.utils.dateparse import parse_date, parse_time

class ReminderTests(APITestCase):
    #Test weather the json response is correct and same as the request.
    def test_create_reminder(self):
        url = reverse('reminder-list')
        data = {
            'email':'dhruv_saini@outlook.com',
            'phone':'7895292663',
            'message':'test_message',
            'date':'2117-03-16',
            'time':'16:00',
        }

        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], 'dhruv_saini@outlook.com')
        self.assertEqual(response.data['phone'], '7895292663')
        self.assertEqual(response.data['message'], 'test_message')
        self.assertEqual(response.data['date'], '2117-03-16')
        self.assertEqual(response.data['time'], '16:00:00')

    #Test to check if ValidationError is returned if datetime is a past value.
    def test_time_can_not_be_past(self):
        url = reverse('reminder-list')
        data = {
            'email':'dhruv_saini@outlook.com',
            'phone':'7895292663',
            'message':'test_message',
            'date':'2117-03-16',
            'time':'16:00',
        }

        response = self.client.post(url, data, format = 'json')
        self.assertTrue(datetime.combine(parse_date(response.data['date']), parse_time(response.data['time'])) > datetime.now())

    #Test to check if ValidationError is returned if no notification method is provided by the user.(Email or SMS)
    def test_provide_either_email_or_phone(self):
        url = reverse('reminder-list')
        data = {
            'message':'test_message',
            'date':'2117-03-16',
            'time':'16:00',
        }

        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #Test when only email is provided by the user.
    def test_provide_only_email(self):
        url = reverse('reminder-list')
        data = {
            'email':'dhruv_saini@outlook.com',
            'message':'test_message',
            'date':'2117-03-16',
            'time':'16:00',
        }

        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #Test when only phone is provided by the user.
    def test_provide_only_phone(self):
        url = reverse('reminder-list')
        data = {
            'phone':'7895292663',
            'message':'test_message',
            'date':'2117-03-16',
            'time':'16:00',
        }

        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
