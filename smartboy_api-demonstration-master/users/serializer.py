from rest_framework import serializers
from rest_framework.response import Response


from .models import User
from location.models import Locations

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'is_admin',
        ]

class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SerializerMethodField('get_loc')

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'is_admin',
            'locations',

        ]
    def get_loc(self, obj):
        from location.serializer import LocationSerializerWithoutUser
        current_id = self.context.get('id')
        queryset = Locations.objects.filter(users=current_id)
        locationserializer = LocationSerializerWithoutUser(queryset, many=True)
        return locationserializer.data

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}  # not to be shown in api view
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            name=self.validated_data['name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password should match'})
        user.set_password(password)
        user.save()
        return user
