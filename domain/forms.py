from django.forms import ModelForm
from .models import File, Event


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
