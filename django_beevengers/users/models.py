from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)


def __str__(self):
    return self.username  # should this return something else? email?
