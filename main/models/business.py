from django.db import models
from django.contrib.auth.models import User

# db model of The venue/business that will be serving drinks
class Business(models.Model):
    SERVICE_TYPES = (
        ('self', 'Self-Service'),
        ('table', 'Table-Service'),
        ('both', 'Self-Service and Table-Service')
    )
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    hours = models.CharField(max_length=255)
    service_type = models.CharField(max_length=25, choices=SERVICE_TYPES)
    drinks_sold = models.IntegerField(default=0)
