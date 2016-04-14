from django.db import models
from .venue import Venue

class Menu(models.Model):
    venue = models.ForeignKey(Venue)
    name = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Item(models.Model):
    CATEGORIES = (
        ('b', 'Beer'),
        ('w', 'Wine'),
        ('m', 'Mixed'),
        ('h', 'Hard Liquor'),
        ('s', 'Soft Drink'),
        ('o', 'Other')
    )
    menu = models.ForeignKey(Menu)
    category = models.CharField(max_length=25, choices=CATEGORIES)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

