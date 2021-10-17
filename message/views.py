from django.shortcuts import render
from .form import InputMessageForm
from .models import InputMessage

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

        output_message = add_emojis(request.POST['body'], 1)

        inputMessage = InputMessage()
        inputMessage.body = output_message
        inputMessage.name = request.POST['name']
        inputMessage.pub_date = timezone.datetime.now()

        if request.user.is_authenticated:
            inputMessage.user = request.user
        elif User.objects.filter(username='default_user').exists():
            inputMessage.user = User.objects.get(username='default_user')
        else:
            User.objects.create(username='default_user',
                                password='Django1234!!')
            inputMessage.user = User.objects.get(username='default_user')

        inputMessage.save()

        return render(request, 'message/confirm.html', {'inputMessage': inputMessage})

    context = {

        'form': form
    }

    return render(request, 'message/home.html', context)


def add_emojis(input_text, magnitude_factor):

    output = ("\U0001f92A" * magnitude_factor)+input_text

    return output


def dashboard(request):
    messages = InputMessage.objects.filter(user=request.user)
    return render(request, 'message/dashboard.html', {'messages': messages})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
