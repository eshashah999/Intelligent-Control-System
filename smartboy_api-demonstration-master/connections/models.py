from django.db import models

class Connections(models.Model):
    connection_name = models.CharField(max_length=20, blank=True, null=True)
    connection_pin = models.IntegerField(default=0)
    #connection_on = models.URLField(default="")
    #connection_off = models.URLField(default="")
    is_high = models.BooleanField(default=False)

    def __str__(self):
        return self.connection_name

class ConnectionUrl(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
