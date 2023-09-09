from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from random import randrange
from django.urls import reverse
from .models import VerifyModel


# Create your views here.


class BaseView(View):

    def get(self, request):
        return render(request, 'base/base.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'base/login.html')

    def post(self, request):
        data = request.POST
        user = authenticate(username=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'base/login.html', context={'message': 'Incorrect email or password'})


class RegistrationView(View):
    EMAIL_HOST_USER = 'otherstest@yandex.ru'

    def get(self, request):
        form = SignUpForm()
        return render(request, 'base/registration.html', context={'form': form})

    def post(self, request):
        if request.POST['stage'] == 'registration':
            form = SignUpForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if self.is_registered(data['email']):
                    return render(request, 'base/registration.html',
                                  context={'form': form, 'message': 'User with this email is already registered'})
                else:
                    code = self.send_code(data['email'])
                    self.create_unregistered_user(data, code)
                    return render(request, 'base/verify.html', context={'username': data['email']})
            else:
                return render(request, 'base/registration.html', context={"form": form})
        else:
            code = request.POST['user_code']
            username = request.POST['username']
            try:
                unregistered_user = VerifyModel.objects.get(username=username, code=code)
            except:
                return render(request, 'base/verify.html', context={'message': 'Invalid code'})
            else:
                registered_user = self.create_registered_user(unregistered_user)
                login(request, registered_user)
                return HttpResponseRedirect('/')

    def is_registered(self, username):
        if len(User.objects.filter(username=username)) > 0:
            return True
        return False

    def send_code(self, email):
        code = randrange(1000, 9999)
        while len(VerifyModel.objects.filter(code=code)) > 0:
            code = randrange(1000, 9999)
        send_mail(
            subject='Code for registration in the Others',
            message=f"{code} - your verification code",
            from_email=RegistrationView.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return code

    def create_unregistered_user(self, data, code):
        values_for_update = {"first_name": data['name'], 'last_name': data['surname'], 'password': data['password'],
                             'code': code}
        VerifyModel.objects.update_or_create(username=data['email'], defaults=values_for_update)

    def create_registered_user(self, unregistered_user):
        User.objects.create_user(username=unregistered_user.username, password=unregistered_user.password,
                                 first_name=unregistered_user.first_name,
                                 last_name=unregistered_user.last_name)
        registered_user = authenticate(username=unregistered_user.username, password=unregistered_user.password)
        unregistered_user.delete()
        return registered_user
