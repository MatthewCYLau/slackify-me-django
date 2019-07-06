from django.shortcuts import render, redirect
from .form import InputMessageForm
from .models import InputMessage
from django.http import HttpResponseRedirect
import requests
import os
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.contrib.auth.models import User


# Create your views here.


def home(request):

    form = InputMessageForm(request.POST or None)

    if request.method == "POST":

        if 'RDS_HOSTNAME' in os.environ:

            auth_token = os.environ['SLACK_AUTH_TOKEN']

        else:
            auth_token = ""

        output_message = add_emojis(request.POST['body'], 1)

        payload = {'channel': request.POST['channel'], 'text': output_message}
        hed = {'Authorization': 'Bearer ' + auth_token}

        requests.post("https://slack.com/api/chat.postMessage", data=payload, headers=hed)

        inputMessage = InputMessage()
        inputMessage.body = output_message
        inputMessage.channel = request.POST['channel']
        inputMessage.name = request.POST['name']
        inputMessage.pub_date = timezone.datetime.now()
        inputMessage.save()

        return render(request, 'message/confirm.html', {'inputMessage': inputMessage})

    context = {

        'form': form
    }

    return render(request, 'message/home.html', context)


def add_emojis(input_text, magnitude_factor):

    output = ("\U0001f92A" * magnitude_factor)+input_text

    return output


def confirm(request):
    return render(request, 'message/confirm.html')


def dashboard(request):
    return render(request, 'message/dashboard.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
