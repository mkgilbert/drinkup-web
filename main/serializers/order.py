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
        # items_data = validated_data.pop('items')
        # print("items_data: " + items_data)
        # #cust_id = validated_data.pop('cust_id')
        # #print("cust_id: " + str(cust_id))
        # #customer = Customer.objects.get(pk=cust_id)
        # order = Order.objects.create(**validated_data)
        # for item_data in items_data:
        #     item_id = int(item_data['item_id'])
        #     qty = int(item_data['item_qty'])
        #     order.add_item(item_id, qty)
        # return order

class ItemOrderLinkSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    order = OrderSerializer()

    class Meta:
        model = ItemOrderLink
        fields = ('id', 'item', 'order', 'item_order_price')

# don't know if i need this
class CreateOrderElement(serializers.Serializer):
    item_id = serializers.IntegerField()
    item_qty = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop('order')
        super(serializers.Serializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        self.order.add_item(int(validated_data['item_id']),
                            int(validated_data['item_qty']))
        return self.order
