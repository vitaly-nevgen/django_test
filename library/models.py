from django.db import models
from django.conf import settings


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bday = models.DateTimeField()

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
