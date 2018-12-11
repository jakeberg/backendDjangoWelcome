from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    bio = models.TextField(max_length=1000)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    time = models.CharField(max_length=50)
    instructions = models.TextField(max_length=2000)

    def __str__(self):
        return self.title