from django.db import models
from django.contrib.auth.models import User


class VerifyModel(models.Model):
    username = models.CharField()
    password = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    code = models.IntegerField(unique=True)

