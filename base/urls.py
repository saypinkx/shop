from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
]
