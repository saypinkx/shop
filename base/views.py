from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from random import randrange


# Create your views here.


class BaseView(View):

    def get(self, request):
        return render(request, 'base/base.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'base/login.html')


class RegistrationView(View):
    EMAIL_HOST_USER = 'otherstest@yandex.ru'

    def get(self, request):
        form = SignUpForm()
        return render(request, 'base/registration.html', context={'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if RegistrationView.is_registered(data['email']):
                return render(request, 'base/registration.html',
                              context={'form': form, 'message': 'User with this email is already registered'})
            else:
                code = RegistrationView.send_code(data['email'])
                request.POST = request.POST.copy()
                request.POST['code'] = code
                return render(request, 'base/verify.html')


        else:
            return render(request, 'base/registration.html', context={"form": form})

    @staticmethod
    def is_registered(username):
        if len(User.objects.filter(username=username)) > 0:
            return True
        return False

    @classmethod
    def send_code(cls, email):
        code = randrange(1000, 9999)
        send_mail(
            subject='Code for registration in the Others',
            message=f"{code} - your verification code",
            from_email=cls.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return code
