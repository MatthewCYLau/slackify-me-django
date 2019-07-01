from django.shortcuts import render
from .form import InputMessageForm
from django.http import HttpResponseRedirect
import requests

# Create your views here.


def home(request):

    form = InputMessageForm(request.POST or None)

    if request.method == "POST":

        auth_token = 'xoxp-140168250439-479776639701-681206313383-915e615b692a685f379ad58b8bbde108'
        payload = {'channel': 'CJGGJBSNM', 'text': request.POST['body']}
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
