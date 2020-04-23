from django.contrib import admin

from connections.models import Connections,ConnectionUrl

admin.site.register(Connections)
admin.site.register(ConnectionUrl)
