from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=150, blank=True, null=False)
