from rest_framework import serializers
from main.models import Customer
from .venue import VenueSerializer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id','name', 'number')

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)