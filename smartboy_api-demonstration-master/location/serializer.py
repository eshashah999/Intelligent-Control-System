from rest_framework import serializers



from connections.serializer import ConnectionListSerializer
from location.models import Locations
from users.models import User
from users.serializer import UserSerializer


class LocationSerializer(serializers.ModelSerializer):
    #is_fav = serializers.SerializerMethodField('getFav')

    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Locations
        fields = [
            'id',
            'location_name',
            'users',
        ]

class LocationAllocationSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.object.all())

    class Meta:
        model = Locations
        fields = [
            'users',
        ]

class LocationSerializerWithoutUser(serializers.ModelSerializer):


    class Meta:
        model = Locations
        fields = [
            'id',
            'location_name',
        ]

    # def getFav(self, obj):
    #     current_id = self.context.get('id')
    #
    #     for id in range(FavByUser.objects.count()):
    #         id += 1
    #         if FavByUser.objects.get(id=id).users.get(id=current_id).id == current_id:
    #             return True
    #         else:
    #             return False

        # test = FavByUser.objects.get(id=1).users.get(id=current_id).id

class LocationConnectionsSerializer(serializers.ModelSerializer):

    connections = ConnectionListSerializer(many=True, read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Locations
        fields = [
            'id',
            'location_name',
            'connections',
            'users'
        ]