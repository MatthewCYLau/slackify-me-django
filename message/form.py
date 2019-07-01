from django import forms
from .models import InputMessage


CHANNEL_CHOICES= [
    ('CJGGJBSNM', 'SE Hackathon 2019'),
    ]


class InputMessageForm(forms.ModelForm):

    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={"placeholder": "Enter name here"}))
    channel = forms.CharField(label='Slack channel', widget=forms.Select(choices=CHANNEL_CHOICES))
    body = forms.CharField(label='Your message', widget=forms.TextInput(attrs={'class':'form-control', "placeholder": "Enter slack message body here"}))

    class Meta:
        model = InputMessage
        fields = [

            'name',
            'channel',
            'body'
        ]
