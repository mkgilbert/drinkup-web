from django.db import models
from .venue import Venue

class Menu(models.Model):
    venue = models.ForeignKey(Venue, related_name='menus')
    name = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.venue.name + ": " + self.name

class Item(models.Model):
    CATEGORIES = (
        ('beer', 'Beer'),
        ('wine', 'Wine'),
        ('mixed', 'Mixed Drink'),
        ('liquor', 'Hard Liquor'),
        ('soft', 'Soft Drink'),
        ('other', 'Other')
    )
    menu = models.ForeignKey(Menu, related_name='items')
    category = models.CharField(max_length=25, choices=CATEGORIES)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    @property
    def get_price_formatted(self):
        return "$" + "{:,.2f}".format(self.price / 100.0)

    def __str__(self):
        return self.name

