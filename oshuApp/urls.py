from django.urls import path
from django.conf import settings
from .views import EventList, EventDetails, MyPage, Login

urlpatterns = [
    path('oshu/EventList', EventList.as_view(), name='EventList'),
    path('oshu/EventDetails', EventDetails.as_view(), name='EventDetails'),
    path('oshu/MyPage', MyPage.as_view(), name='MyPage'),
    path('oshu/Login', Login.as_view(), name='Login'),
]
