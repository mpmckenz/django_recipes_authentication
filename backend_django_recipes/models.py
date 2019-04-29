from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    def __str__(self):
        return self.name
    pass


class Recipes(models.Model):
    pass
