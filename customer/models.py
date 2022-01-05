from django.contrib.sessions.models import Session
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=False)

