from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):

    list_display = ('name', 'venue', 'date', 'time')
    fields = ('group', 'name', 'user', 'details', 'venue', ('date', 'time'))
    search_fields = ('name', 'details')

admin.site.register(Event, EventAdmin)

