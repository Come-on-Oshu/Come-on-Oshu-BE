# api
from rest_framework.views import APIView
from rest_framework.response import Response
# authentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# models, serializers
from .models import EventInformation, EventLocation, InterestEvent
from .serializers import EventInformationSerializer, EventLocationSerializer, EventDetailInfoSerializer


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
        # use serializer to change DB object to json
        event_info = EventDetailInfoSerializer(event_info)

        return Response(event_info.data)


class MyPage(APIView):
    def get(self, request):
        # get the request variable : id(uesr_id)
        user_id = request.query_params.get('id')
        # get the same object as the request variable(user id) from DB
        userinfo = User.objects.get(username=user_id)
        # get the list of interest of the request user
        eid_list = InterestEvent.objects.filter(userid__username__contains=user_id)

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
        # Check user who registerd as member by using received ID and PW and django authentication function
        user = authenticate(username=request.data['id'], password=request.data['pw'])
        # get user's token
        token = Token.objects.get(user=user)
        
        return Response({
            "Token": token.key
        })