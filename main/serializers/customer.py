from rest_framework import serializers
from main.models import Customer
from .venue import VenueSerializer

class CustomerSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'venue', 'name', 'number')

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)