from django.core.validators import RegexValidator
from django.db import models
from .venue import Venue

# db model of The employee/bartender/server that will be serving drinks
class Employee(models.Model):
    venue = models.ForeignKey(Venue, related_name='employees')
    pin_regex = RegexValidator(regex=r'^\d{4}$',
                                message="employee pin must be 4 digits")
    # employs the above defined regex
    pin = models.CharField(max_length=4, validators=[pin_regex], null=False, blank=False)
    name = models.CharField(max_length=25, default="")

    def get_avg_order_time(self):
        orders = self.orders.all()
        num_orders = len(orders)
        seconds_sum = 0
        for order in orders:
            secs = order.get_time_to_complete
            if secs is not None:
                seconds_sum += order.get_time_to_complete
        if seconds_sum > 0:
            return int(seconds_sum / num_orders)
        else:
            return 0

    def __str__(self):
        if self.name == "":
            return str(self.pin)
        return self.name + " (" + str(self.pin) + ")"