from django.contrib import admin

from .models import EventInformation, EventLocation, User, InterestEvent

admin.site.register(EventInformation)
admin.site.register(EventLocation)
admin.site.register(User)
admin.site.register(InterestEvent)