from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# db model of The employee/bartender/server that will be serving drinks
class Employee(models.Model):

    pin_regex = RegexValidator(regex=r'^\d{4}$',
                                message="employee pin must be 4 digits")
    # employs the above defined regex
    pin = models.CharField(max_length=4, validators=[pin_regex], null=False, blank=False)
    name = models.CharField(max_length=255)

