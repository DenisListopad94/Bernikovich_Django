from django.db import models
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from models import MyModel
from django.db import models
from django.contrib.auth.models import User


class MyModel(models.Model):
    class Meta:
        permissions = (
            ("view_mymodel", "Can view my model"),
            ("change_mymodel", "Can change my model"),
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.FileField(upload_to='info/', null=True, blank=True)


def clear_cache():
    cache.clear()


# Сигнал, который будет вызван после сохранения объекта модели MyModel
@receiver(post_save, sender=MyModel)
@permission_required('myapp.view_model', raise_exception=True)
def my_view():
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user=self)
