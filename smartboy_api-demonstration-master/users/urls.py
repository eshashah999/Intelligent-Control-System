from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserListView, CurrentUserIdView, CurrentUserView, UserRegistrationView

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('createuser', UserRegistrationView.as_view(),name='create user'),
    path('userlist', UserListView.as_view(), name='userlist'),
    path('user/<int:id>', CurrentUserIdView.as_view(), name='user with id'),
    path('user', CurrentUserView.as_view(), name='Current User')


]