from calendar import FRIDAY, THURSDAY
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)

class Event(models.Model):
# TODO: implement difirent categories for events
    event_name = models.TextField()

class SheduledUsersEvents(models.Model):
    class WEEKDAYS(models.TextChoices):
        SUNDAY = 'su', 'Sunday'
        MONDAY = 'mo', 'Monday'
        TUESDAY = 'tu', 'Tuesday'
        WEDNESDAY = 'we', 'Wednesday'
        THURSDAY = 'th', 'Thursday'
        FRIDAY = 'fr', 'Friday'
        SATURDAY = 'sa', 'Saturday'

    username = models.ForeignKey('User', on_delete=models.CASCADE, related_name='schedule')
    event_name = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='schedule')
    weekdays = models.TextField(choices=WEEKDAYS.choices, null=False, blank=False)
