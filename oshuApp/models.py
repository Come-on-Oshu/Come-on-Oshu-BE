from django.db import models


class EventInformation(models.Model):
    District = models.IntegerField() #행사 지역구
    EventName = models.TextField() #행사 이름
    isFestival = models.IntegerField() #행사 or 축제 여부
    ImgUrl = models.TextField() #행사 포스터 이미지 url
    stDate = models.DateTimeField() #행사 시작 날짜
    edDate = models.DateTimeField() #행사 끝 날짜
    Organization = models.TextField() #행사 주체 기관
    Location = models.TextField() #행사 위치
    WebsiteUrl = models.TextField() #행사 안내 웹사이트 url
