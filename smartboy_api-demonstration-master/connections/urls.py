from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from connections.views import ConnectionListView, ConnectionStatusUpdateView

urlpatterns = [
    path('connections', ConnectionListView.as_view(), name='connection List'),
    path('connection/<int:id>', ConnectionStatusUpdateView.as_view(), name='specific connection'),


]