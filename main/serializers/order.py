from rest_framework import serializers
from main.models import (Order, ItemOrderLink)
from .menu import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    time_created = serializers.DateTimeField()
    time_completed = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ('id', 'time_created', 'time_completed', 'is_paid', 'items')


class ItemOrderLink(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    order = OrderSerializer()

    class Meta:
        model = ItemOrderLink
        fields = ('id', 'item', 'order', 'quantity', 'item_order_price')