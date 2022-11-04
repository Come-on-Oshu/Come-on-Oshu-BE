import request
from rest_framework.utils import json

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventInformation, EventLocation, User, InterestEvent
from .serializers import EventInformationSerializer, EventLocationSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class EventList(APIView):
    def get(self, request):
        # get the request variable : district
        district = request.query_params.get('district')
        # get the same object(EventInformation) as the request variable from DB
        EI_list = EventInformation.objects.filter(District=district)
        # use serializer to change DB object to json
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
        user_id = request.query_params.get('userid')
        userinfo = User.objects.get(userid=user_id)
        eid_list = InterestEvent.objects.filter(userid__userid__contains=user_id)

        return_list = list()
        for item in eid_list:
            EI = EventInformation.objects.filter(eid=item.eid.eid)
            for j in EI:
                EIserializer = EventInformationSerializer(j)
                return_list.append(EIserializer.data)

        return Response({
            "username": userinfo.username,
            "InterestEventList": return_list
        })


class Login(APIView):
    def get(self, request):
        user = authenticate(username=request.data['id'], password=request.data['pw'])

        token = Token.objects.get(user=user)
        return Response({
            "Token": token.key
        })