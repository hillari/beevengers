from django.db import models


class Subscription(models.Model):
    email = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.email
