from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(name='email', unique=True)
    first_name = models.CharField(name='name', max_length=30)
    last_name = models.CharField(name='surname',max_length=30)
    date_joined = models.DateTimeField(name='registered', auto_now_add=True)
    is_active = models.BooleanField(name='is_active', default=True)
    number = models.CharField(name='number')
    password = models.CharField(name='password', max_length=30)
    objects = UserManager()

