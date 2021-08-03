
from django.forms import ModelForm

from homes.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'text']
