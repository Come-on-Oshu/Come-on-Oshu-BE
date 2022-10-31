from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView
from django.shortcuts import render
import request
import secret

class PostList(ListView):
    def index(request):
        url = 'http://apis.data.go.kr/6300000/festivalDaejeonService/festivalDaejeonList'
        params = {'serviceKey': secret.key, 'searchCondition': '', 'searchKeyword': '', 'pageNo': '1', 'numOfRows': '10'}

        response = requests.get(url, params=params)
        print(response.content)

        return render(
            request,
            'main.html',
            {

            }
        )