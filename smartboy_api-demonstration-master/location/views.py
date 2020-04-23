from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from location.models import Locations
from location.serializer import LocationConnectionsSerializer, LocationSerializer, LocationAllocationSerializer


class LocationConnectionListView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, id):
        query_set = Locations.objects.get(id=id)
        locationConnectionListSerializer = LocationConnectionsSerializer(query_set)
        return Response(locationConnectionListSerializer.data)

class AllocateLocationView(APIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAdminUser, ]

    def put(self, request, id, format=None):
        queryset = Locations.objects.get(id=id)
        allotlocationserializer = LocationAllocationSerializer(queryset, data=request.data)
        data = {}

        if allotlocationserializer.is_valid():
            allocated_location = allotlocationserializer.save()
            data['Location Alloted'] = 'Success'
            data['users_added'] = allotlocationserializer.data
            return Response(data)
        else:
            return Response(allotlocationserializer.errors)


