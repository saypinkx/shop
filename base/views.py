from django.shortcuts import render
from django.views import View
# Create your views here.


class BaseView(View):
    def get(self, request):
        return render(request, 'base/base.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'base/login.html')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'base/registration.html')