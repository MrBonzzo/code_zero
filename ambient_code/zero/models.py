from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Event(models.Model):
# TODO: implement difirent categories for events
    event_name = models.TextField()

    def __str__(self):
        return self.event_name
class SheduledUsersEvents(models.Model):
    class WEEKDAYS(models.TextChoices):
        SUNDAY = 'su', 'Sunday'
        MONDAY = 'mo', 'Monday'
        TUESDAY = 'tu', 'Tuesday'
        WEDNESDAY = 'we', 'Wednesday'
        THURSDAY = 'th', 'Thursday'
        FRIDAY = 'fr', 'Friday'
        SATURDAY = 'sa', 'Saturday'

    username = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='User name', related_name='schedule')
    event_name = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='schedule')
    weekdays = models.TextField(choices=WEEKDAYS.choices, null=False, blank=False)
