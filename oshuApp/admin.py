from django.contrib import admin

from .models import EventInformation, EventLocation, InterestEvent, Profile

admin.site.register(EventInformation)
admin.site.register(EventLocation)
admin.site.register(Profile)
admin.site.register(InterestEvent)