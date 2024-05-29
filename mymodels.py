from django.db import models
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class MyModel(models.Model):
    class Meta:
        permissions = (
            ("view_mymodel", "Can view my model"),
            ("change_mymodel", "Can change my model"),
        )


@permission_required('myapp.view_mymodel', raise_exception=True)
def my_view():
    pass


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user=self)
