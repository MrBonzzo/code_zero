from secrets import choice
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from zero.models import SheduledUsersEvents
from zero.forms import AddEventForm

def index(request):
    template_name = 'zero/index.html'
    context = {
        'events': SheduledUsersEvents.objects.all(),
    }
    return render(request, template_name=template_name, context=context)

class AddEventView(CreateView):
    template_name = 'zero/add_event.html'
    form_class = AddEventForm
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['weekday'] = SheduledUsersEvents.WEEKDAYS.choices
    #     return context