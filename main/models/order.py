from datetime import datetime
from django.db import models
from .venue import Venue
from .menu import Item
from .customer import Customer
from .employee import Employee
from .item_order_link import ItemOrderLink

"""
An order that consists of 1 or many items. You must use the ItemOrderLink table to connect
the 2 though.
"""
class Order(models.Model):
    PAYMENT_TYPES = (
        ('cc', 'Credit Card'),
        ('cs', 'Cash'),
        ('ck', 'Check')
    )
    time_created = models.DateTimeField(auto_now_add=True)
    time_completed = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False, blank=True)
    is_delivered = models.BooleanField(default=False, blank=True)
    payment_type = models.CharField(max_length=3, choices=PAYMENT_TYPES, default='cs',
                                    null=True, blank=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, related_name='orders')
    employee = models.ForeignKey(Employee, blank=True, null=True, related_name='orders')
    items = models.ManyToManyField(Item, through='ItemOrderLink')
    venue = models.ForeignKey(Venue, related_name='orders')

    def get_total(self):
        """
        Gets total price of the order by adding up all prices of items
        :return: integer
        """
        links = ItemOrderLink.objects.filter(order=self)
        total = 0
        for link in links:
            total += (link.item_order_price * link.quantity)
        return total

    @property
    def get_total_formatted(self):
        return "$" + "{:,.2f}".format(self.get_total() / 100.0)

    def add_item(self, item_id, qty):
        """
        Must be used because we're using a "through" intermediary table (ItemOrderLink) instead of letting
        Django take care of that for us. We can't use the .add() method like usual, so we can do this instead
        to add items to the order.
        :param item: Item model object that you want to add to the order
        :param qty: Integer quantity of the Item object you want to add
        :return: Returns ItemOrderLink object
        """
        item = Item.objects.get(pk=item_id)
        return ItemOrderLink.objects.create(order=self, item=item, quantity=qty,
                                        item_order_price=item.price)

    def get_item_links(self):
        return ItemOrderLink.objects.filter(order = self)

    def complete_all_items(self):
        links = self.get_item_links()
        for link in links:
            link.status = "complete"
            link.save()
        self.time_completed = datetime.now()
        self.save()