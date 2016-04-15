from rest_framework import serializers
from main.models import Employee
from .venue import VenueSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'venue', 'pin', 'name')