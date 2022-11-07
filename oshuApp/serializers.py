from rest_framework import serializers
from .models import EventInformation, EventLocation


class EventInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInformation
        fields = ('eid', 'EventID', 'District', 'EventName', 'isFestival', 'ImgUrl', 'stDate', 'edDate', 'Organization', 'lid')

class EventDetailInfoSerializer(serializers.ModelSerializer):
    SiteUrl = serializers.SerializerMethodField('get_SiteUrl')
    address = serializers.SerializerMethodField('get_address')

    def get_address(self, obj):
        lid = obj.lid
        event_loca = EventLocation.objects.get(lid=lid.lid)
        return event_loca.address

    def get_SiteUrl(self, obj):
        lid = obj.lid
        event_loca = EventLocation.objects.get(lid=lid.lid)
        return event_loca.SiteUrl

    class Meta:
        model = EventInformation
        fields = ('EventID', 'EventName', 'isFestival', 'ImgUrl', 'stDate', 'edDate', 'Organization', 'address', 'SiteUrl')


class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = ('lid', 'LocationID', 'LocationName', 'Telno', 'SiteUrl', 'address', 'la', 'lo')