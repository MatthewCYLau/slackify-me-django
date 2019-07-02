from django.shortcuts import render
from .form import InputMessageForm
from django.http import HttpResponseRedirect
import requests
import os

# Create your views here.


def home(request):

    form = InputMessageForm(request.POST or None)

    if request.method == "POST":

        if 'RDS_HOSTNAME' in os.environ:

            auth_token = os.environ['SLACK_AUTH_TOKEN']

        else:
            pass

        payload = {'channel': request.POST['channel'], 'text': request.POST['body']}
        hed = {'Authorization': 'Bearer ' + auth_token}

        r = requests.post("https://slack.com/api/chat.postMessage", data=payload, headers=hed)

        form.save()

        return HttpResponseRedirect('message/confirm')

    context = {

        'form': form
    }

    return render(request, 'message/home.html', context)


def confirm(request):
    return render(request, 'message/confirm.html')
