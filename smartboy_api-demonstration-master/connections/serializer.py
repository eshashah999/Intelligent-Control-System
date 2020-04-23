from rest_framework import serializers

from connections.models import Connections,ConnectionUrl


class ConnectionListSerializer(serializers.ModelSerializer):
    connection_url = serializers.SerializerMethodField('getUrl')
    class Meta:
        model = Connections
        fields = [
            'id',
            'connection_name',
            'connection_pin',
            'connection_url',
            'is_high',
        ]

    def getUrl(self, obj):
        queryset = ConnectionUrl.objects.get(id=1)
        return str(queryset)


class ConnectionStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connections
        fields = [
            'is_high',
        ]