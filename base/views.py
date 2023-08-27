from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import SignUpForm

# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, 'base/base.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'base/login.html')


class RegistrationView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'base/registration.html', context={'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/registration')
        else:
            return render(request, 'base/registration.html', context={"form": form})



