from django.urls import path
from django.conf import settings
from .views import EventList

urlpatterns = [
    path('oshu/Event', EventList.as_view(), name='EventList'),
]
