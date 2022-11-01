from django.contrib import admin

from .models import EventInformation, EventLocation

admin.site.register(EventInformation)
admin.site.register(EventLocation)