from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializer import UserSerializer, UserRegistrationSerializer,UserListSerializer


class UserListView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        query_set = User.object.all()
        # query_set = User.object.get(id=1)
        userListSerializer = UserListSerializer(query_set, many=True, read_only=True)
        content = {'users': userListSerializer.data}
        return Response(content)

class CurrentUserView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        #query_set = User.object.get(id=id)
        userSerializer = UserSerializer(request.user, context={'id': request.user.id}) #to get current user
        return Response(userSerializer.data)


class CurrentUserIdView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request, id):
        query_set = User.object.get(id=id)
        userSerializer = UserSerializer(query_set, many=False)
        return Response(userSerializer.data)


class UserRegistrationView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        user_register_serializer = UserRegistrationSerializer(data=request.data)

        data = {}
        if user_register_serializer.is_valid():
            user = user_register_serializer.save()
            data['response'] = 'success'
            data['username'] = user.username
            data['name'] = user.name
            token = Token.objects.get(user=user).key
            data['token'] = token
            return Response(data)
        else:
            return Response(user_register_serializer.errors)