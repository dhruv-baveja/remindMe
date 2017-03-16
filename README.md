# RemindMe

RemindMe is a webapi in which Anybody can provide either their email address or their mobile number or both and setup a reminder with a message. RemindMe then reminds them over their preferred channel of notification with the message.  

## Getting Started:

Start Redis server:
```sh
redis-server
```

Start Celery worker
```sh
python manage.py celeryd
```
>celery is used for creating background task to send notification at the scheduled time.


Start Django
```sh
python manage.py runserver.
```

## API Endpoint:

```sh
RemindMe/reminders/
```

API Fields:
```sh
{
  "email": "user@email.com",
  "phone": "Phone No",
  "message": "Remind me to call abc.",
  "date": "2017-03-16",
  "time": "11:30",
}
```

Note: provides list, create, retrieve, update and destroy actions.


Reminder URL:
```sh
/reminders/id/
```

Reminder Message URL:
```sh
/reminders/id/title
```
## Requirements:
Django 1.8.2
Python 3.5
Redis 2.8
Celery 4.0



Note: SMS function is only a dummy function. It does not actually send a sms.
