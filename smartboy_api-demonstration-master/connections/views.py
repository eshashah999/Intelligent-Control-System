
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from connections.models import Connections
from connections.serializer import ConnectionListSerializer,ConnectionStatusSerializer


class ConnectionListView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        query_set = Connections.objects.all().order_by('-id')
        connectionListSerializer = ConnectionListSerializer(query_set, many=True)
        return Response(connectionListSerializer.data)

class ConnectionStatusUpdateView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def put(self, request, id):
        query_set = Connections.objects.get(id=id)
        connectionStatusSerializer = ConnectionStatusSerializer(query_set, data=request.data)
        data = {}
        if connectionStatusSerializer.is_valid():
            updatedConnection = connectionStatusSerializer.save()
            data['status_updated'] = connectionStatusSerializer.data
            return Response(data)
        else:
            return Response(connectionStatusSerializer.errors)






