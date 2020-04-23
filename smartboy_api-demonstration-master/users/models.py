from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from smartboy_api import settings


class MyUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username='', name='', password=None):
        user = self.model(
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, password, username='', name=''):
        user = self.create_user(

            password=password,
            username=username,
            name=name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=20)
    username = models.CharField(max_length=10, unique=True)
    # locations = models.ManyToManyField('location.Locations', default=None, blank=True, null=True)

    # REQUIRED FIELDS (DON'T TOUCH)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last logined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # login field
    REQUIRED_FIELDS = ['name',]

    object = MyUserManager()

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)