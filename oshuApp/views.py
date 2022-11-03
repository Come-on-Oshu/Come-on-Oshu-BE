import request

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventInformation

class EventList(APIView):
    def get(self, request):
        district = request.query_params.get('district')
        print(district)
        # El = EventInformation.objects.get(District=district)
        # print(El.EventID)

        list = EventInformation.objects.filter(District=district)
        print(list)

        return Response({
            "d":"d",
            "o":list
        })


