from rest_framework import serializers
from main.models import (Order, Item, ItemOrderLink, Customer, Employee)
from .menu import ItemSerializer
from .customer import CustomerSerializer
from .venue import VenueSerializer
from .employee import EmployeeSerializer


class ItemOrderLinkSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='item.id')
    name = serializers.ReadOnlyField(source='item.name')
    link_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = ItemOrderLink
        fields = ('id', 'link_id', 'name', 'status', 'quantity', 'item_order_price')

class OrderSerializer(serializers.ModelSerializer):
    time_created = serializers.DateTimeField()
    time_completed = serializers.DateTimeField()
    customer = CustomerSerializer()
    venue = VenueSerializer()
    employee = EmployeeSerializer()
    items = ItemOrderLinkSerializer(source='itemorderlink_set', many=True)

    class Meta:
        model = Order
        fields = ('id', 'venue', 'customer', 'employee', 'time_created',
                  'time_completed', 'is_delivered', 'is_paid', 'items')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(type(validated_data))
        time_comp = validated_data.get('time_completed')
        is_del = validated_data.get('is_delivered')
        if time_comp is not None:
            instance.time_completed = validated_data.get('time_completed', instance.time_completed)
        if is_del is not None:
            instance.is_delivered = validated_data.get('is_delivered', instance.is_delivered)
        instance.save()
        return instance


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
