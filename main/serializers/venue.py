from rest_framework import serializers
from main.models import Venue

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('phone', 'name', 'address', '_lat', '_lon', 'description',
                  'website', 'hours', 'service_type')