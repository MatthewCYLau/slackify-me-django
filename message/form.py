from django import forms
from .models import InputMessage


class InputMessageForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter name here"}))
    channel = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Enter email here"}))
    body = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', "placeholder": "Enter body here"}))

    class Meta:
        model = InputMessage
        fields = [

            'name',
            'channel',
            'body'
        ]
