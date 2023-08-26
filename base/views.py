from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm


# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, 'base/base.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'base/login.html')


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'base/registration.html', context={'form': form})
