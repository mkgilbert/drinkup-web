from django.db import models
from .menu import Item

"""
Acts as intermediary table between items and orders due to the many-to-many relationship
"""
class ItemOrderLink(models.Model):
    item = models.ForeignKey(Item, null=True)
    order = models.ForeignKey('Order', null=True)
    status = models.CharField(max_length=20, default="incomplete")
    quantity = models.IntegerField(default=1)
    item_order_price = models.IntegerField(null=True, blank=True)

    @property
    def format(self):
        return "$" + "{:,.2f}".format(self.item_order_price * self.quantity / 100.0)

