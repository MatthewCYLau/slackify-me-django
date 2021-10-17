from django import forms
from .models import InputMessage


class InputMessageForm(forms.ModelForm):

    name = forms.CharField(label='Your name', widget=forms.TextInput(
        attrs={"placeholder": "Enter name here"}))
    body = forms.CharField(label='Your message', widget=forms.TextInput(
        attrs={'class': 'form-control', "placeholder": "Enter slack message body here"}))

    class Meta:
        model = InputMessage
        fields = [

            'name',
            'body',
        ]
