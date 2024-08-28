from django.contrib import admin
from .models import *

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'organizer', 'image', 'category', 'time', 'created_at')
    search_fields = ('title', 'category', 'organizer')
    readonly_fields = ('created_at', 'time')
    
admin.site.register(Event, EventAdmin)