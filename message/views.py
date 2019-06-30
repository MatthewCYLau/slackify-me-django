from django.shortcuts import render
from .form import InputMessageForm
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):

    form = InputMessageForm(request.POST or None)

    if request.method == "POST":
        form.save()
        form = InputMessageForm()

        return HttpResponseRedirect('home')

    context = {

        'form': form
    }

    return render(request, 'message/home.html', context)


def form(request):

    form = InputMessageForm(request.POST or None)

    if request.method == "POST":

        form.save()
        form = InputMessageForm()

        return HttpResponseRedirect('home')

    context = {

        'form': form
    }

    return  render(request, 'message/form.html', context)
