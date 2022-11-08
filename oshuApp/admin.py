from django.contrib import admin

from .models import EventInformation, EventLocation, InterestEvent, User

admin.site.register(EventInformation)
admin.site.register(EventLocation)
admin.site.register(InterestEvent)
admin.site.register(User)