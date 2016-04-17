from rest_framework import serializers
from main.models import Employee
from .venue import VenueSerializer

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name')