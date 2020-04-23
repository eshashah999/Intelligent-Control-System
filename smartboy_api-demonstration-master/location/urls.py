from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from location.views import LocationConnectionListView,AllocateLocationView

urlpatterns = [
    path('location/<int:id>', LocationConnectionListView.as_view(), name='labs connections'),
    path('location/<int:id>/addusers', AllocateLocationView.as_view(), name='add labs to user'),
]