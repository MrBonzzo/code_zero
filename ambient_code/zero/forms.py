from django.forms import ModelForm
from zero.models import SheduledUsersEvents

class AddEventForm(ModelForm):
    class Meta:
        model = SheduledUsersEvents
        fields = (
            "username", "event_name", "weekdays",
        )