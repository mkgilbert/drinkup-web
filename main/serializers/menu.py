from rest_framework import serializers
from main.models import (Menu, Item)
from .venue import VenueSerializer


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'price', 'menu')