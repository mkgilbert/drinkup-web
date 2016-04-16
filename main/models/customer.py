from django.db import models
from .venue import Venue

class Customer(models.Model):
    venue = models.ForeignKey(Venue, related_name='customers')
    name = models.CharField(max_length=25, default="", null=True, blank=True)
    number = models.IntegerField() # either table number or wristband number

    def __str__(self):
        s = ""
        if self.name != "":
            s += self.name + " "
        return s + str(self.number)