from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# db model of The venue/business that will be serving drinks
class Venue(models.Model):
    SERVICE_TYPES = (
        ('self', 'Self-Service'),
        ('table', 'Table-Service'),
        ('both', 'Self-Service and Table-Service')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                message="Phone number must be in the format '9285551234' and must be exactly 10 digits.")
    # employs the above defined regex
    phone = models.CharField(max_length=10, validators=[phone_regex], null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    _lat = models.FloatField()
    _lon = models.FloatField()
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    hours = models.CharField(max_length=255, null=True, blank=True)
    service_type = models.CharField(max_length=25, choices=SERVICE_TYPES)
    drinks_sold = models.IntegerField(default=0)
