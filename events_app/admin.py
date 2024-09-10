from django.contrib import admin
from .models import Event, Venue, MyClubUser


@admin.register(Event)
class MyEvent(admin.ModelAdmin):
    fields = (('name','venue'), 'event_date', 'description')
    list_display =  ['name','venue', 'event_date', 'description']
    ordering = ('-event_date', )
    list_filter = ('event_date', 'venue')


@admin.register(Venue)
class MyVenue(admin.ModelAdmin):
    list_display = ['name', 'address', 'zip_code', 'phone', 'web', 'email_address']
    ordering = ('name', )
    search_fields = ('adress', 'name')



class MyAdminUser(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']
    ordering = ('-firstname', )

admin.site.register(MyClubUser, MyAdminUser)