from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(MyClubUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=('name','address')
    ordering=['name']
    search_fields=['name','address']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=['name','event_date','venue','manager']
    list_display=['name','event_date']
    ordering=['-event_date']
    list_filter=['event_date','venue']