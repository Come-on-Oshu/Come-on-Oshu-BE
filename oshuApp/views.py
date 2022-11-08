# api
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# authentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# models, serializers
from .models import EventInformation, EventLocation, InterestEvent, User
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

        userid = request.query_params.get('userid')
        user = User.objects.get(userID=userid)
        interest_event_list = InterestEvent.objects.filter(userID=userid)

        return_list = list()
        for item in interest_event_list:
            EI = EventInformation.objects.filter(EventID=item.eventID)
            for j in EI:
                event_info = EventDetailInfoSerializer(j)
                return_list.append(event_info.data)

        return Response({
            "username": user.userName,
            "InterestEventList": return_list
        })


class Login(APIView):
    def get(self, request):

        userid = request.query_params.get('id')
        password = request.query_params.get('pw')

        return_message = {
            'status': -1,
            'message': ''
        }

        try:
            user = User.objects.get(userID=userid)
        except User.DoesNotExist:
            return_message['status'] = 0
            return_message['message'] = 'id가 없습니다'
            return Response(return_message)

        if (user.userPW == password):
            return_message['status'] = 1
            return_message['message'] = "login 성공"
        else:
            return_message['status'] = 2
            return_message['message'] = "비밀번호가 일치하지 않습니다."

        return Response(return_message)


class AddInterestEvent(APIView):
    def post(self, request):
        userid = request.query_params.get('userid')
        eventid = request.query_params.get('eventid')

        Interest_event = InterestEvent()
        Interest_event.userID = userid
        Interest_event.eventID = eventid
        Interest_event.save()

        return Response(status=200)