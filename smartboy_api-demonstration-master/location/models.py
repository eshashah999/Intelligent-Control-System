from django.db import models

from connections.models import Connections


class Locations(models.Model):

    location_name = models.CharField(max_length=10)
    connections = models.ManyToManyField('connections.Connections', default=None, blank=True, null=True)
    users = models.ManyToManyField('users.User', default=None, blank=True, null=True)

    def __str__(self):
        return self.location_name

# class FavByUser(models.Model):
#     location = models.OneToOneField('location.Locations', on_delete=models.CASCADE, default=None, blank=True, null=True)
#     users = models.ManyToManyField('users.User', default=None, blank=True, null=True)
