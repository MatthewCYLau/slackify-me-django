from django.shortcuts import render, redirect
from .form import InputMessageForm
from django.http import HttpResponseRedirect
import requests
import os
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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
