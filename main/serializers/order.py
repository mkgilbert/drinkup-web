from rest_framework import serializers
from main.models import (Order, Item, ItemOrderLink, Customer)
from .menu import ItemSerializer
from .customer import CustomerSerializer
from .venue import VenueSerializer

class OrderSerializer(serializers.ModelSerializer):
    time_created = serializers.DateTimeField()
    time_completed = serializers.DateTimeField()
    customer = CustomerSerializer()
    venue = VenueSerializer()
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'venue', 'customer', 'employee', 'time_created', 'time_completed', 'is_paid', 'items')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

class ItemOrderLinkSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    order = OrderSerializer()

    class Meta:
        model = ItemOrderLink
        fields = ('id', 'item', 'order', 'item_order_price')


class CreateOrderElement(serializers.Serializer):
    """
    This class is super important! I couldn't get orders to be created via the api
    because I needed to make an order using a customer and venue object and then add
    a bunch of items to it. Well, it turns out that the only way I could make it work is
    by creating this funky little serializer CreateOrderElement in order to create the order
    and add all the itmes we want to it. I had to override the __init__ method in order to
    shove in an Order object instance that can have items added it to. So this class just
    serializes item ids and quantities into items by adding them to the self.order instance
    """
    item_id = serializers.IntegerField()
    item_qty = serializers.IntegerField()


    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop('order')
        super(serializers.Serializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        self.order.add_item(int(validated_data['item_id']),
                            int(validated_data['item_qty']))
        return self.order
