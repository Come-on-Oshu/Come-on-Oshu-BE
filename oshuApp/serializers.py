from rest_framework import serializers
from .models import EventInformation, EventLocation


class EventInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInformation
        fields = ('eid', 'EventID', 'District', 'EventName', 'isFestival', 'ImgUrl', 'stDate', 'edDate', 'Organization', 'lid')


class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = ('lid', 'LocationID', 'LocationName', 'Telno', 'SiteUrl', 'address', 'la', 'lo')