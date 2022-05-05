from django.urls import path

from zero.views import index, AddEventView

urlpatterns = [
    path('', index, name='index'),
    path('add/', AddEventView.as_view(), name='add')
]
