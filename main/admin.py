from django.contrib import admin
from main.models import Venue

class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'description', 'website', )
