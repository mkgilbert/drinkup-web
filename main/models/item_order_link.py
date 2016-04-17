from django.db import models
from .menu import Item

"""
Acts as intermediary table between items and orders due to the many-to-many relationship
"""
class ItemOrderLink(models.Model):
    item = models.ForeignKey(Item, null=True)
    order = models.ForeignKey('Order')
    quantity = models.IntegerField(default=1)
    item_order_price = models.IntegerField()

    @property
    def format(self):
        return "$" + "{:,.2f}".format(self.item_order_price * self.quantity / 100.0)

