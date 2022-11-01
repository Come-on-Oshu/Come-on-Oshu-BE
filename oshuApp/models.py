from django.db import models


class EventLocation(models.Model):
    lid = models.AutoField(primary_key=True)
    LocationID = models.TextField(unique=True) #행사 공연 시설 ID
    LocationName = models.TextField() #시설명
    Telno = models.TextField() #시설 전화번호
    SiteUrl = models.TextField(null=True, blank=True) #시설 안내 사이트
    address = models.TextField() #시설 주소(시-구-동)
    la = models.TextField() #시설 위도
    lo = models.TextField() #시설 경도


class EventInformation(models.Model):
    eid = models.AutoField(primary_key=True)
    EventID = models.TextField() #행사 ID
    District = models.TextField() #행사 지역구
    EventName = models.TextField() #행사 이름
    isFestival = models.IntegerField() #행사 or 축제 여부
    ImgUrl = models.TextField() #행사 포스터 이미지 url
    stDate = models.TextField() #행사 시작 날짜
    edDate = models.TextField() #행사 끝 날짜
    Organization = models.TextField() #행사 주체 기관
    lid = models.ForeignKey(EventLocation, on_delete=models.SET_NULL, null=True) #행사 위치