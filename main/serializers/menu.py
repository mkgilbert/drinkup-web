from rest_framework import serializers
from main.models import (Menu, Item)
from .venue import VenueSerializer


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'price')

class MenuSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Menu
        fields = ('id', 'name', 'items')

