from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    class Types(models.TextChoices):
        pass

    def get_absolute_url(self):
        return reverse("users:detail")
