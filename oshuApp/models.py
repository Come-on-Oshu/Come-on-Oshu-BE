from django.db import models


class EventInformation(models.Model):
    District = models.IntegerField()
    EventName = models.TextField()
    isFestival = models.IntegerField()
    ImgUrl = models.TextField()
    stDate = models.DateTimeField()
    enDate = models.DateTimeField()
    Organization = models.TextField()
    Location = models.TextField()
    WebsiteUrl = models.TextField()
    