from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_subscriber = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bday = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{}, {}".format(
            self.first_name, self.last_name
        )

    def get_user_username(self):
        if self.created_by:
            return self.created_by.username


class Book(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
