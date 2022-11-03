import request

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventInformation, EventLocation
from .serializers import EventInformationSerializer, EventLocationSerializer


class EventList(APIView):
    def get(self, request):
        # get the request variable : district
        district = request.query_params.get('district')
        # get the same object(EventInformation) as the request variable from DB
        EI_list = EventInformation.objects.filter(District=district)
        # use serializer to change DB object to json
        serializer = EventInformationSerializer(EI_list)
        # variable to store event lists
        event_list = list()
        for item in EI_list:
            serializer = EventInformationSerializer(item)
            event_list.append(serializer.data)

        return Response(event_list)

class EventDetails(APIView):
    def get(self, request):
        # get the request variable : eventid
        eventid = request.query_params.get('eventid')
        # get the same object as the request variable(eventid) from DB
        event_info = EventInformation.objects.get(EventID=eventid)
        # becouse of FK, can obtain location info related to event
        lid = event_info.lid
        # use serializer to change DB object to json
        serializer_EI = EventInformationSerializer(event_info)
        serializer_EL = EventLocationSerializer(lid)
        # variable to store event lists
        eventdetails = list()
        eventdetails.append(serializer_EI.data)
        eventdetails.append(serializer_EL.data)

        return Response(eventdetails)

class MyPage(APIView):
    def get(self, request):
        


