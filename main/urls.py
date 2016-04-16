from django.conf.urls import url
from main.views.api import (customer, venue)

urlpatterns = [
    url(r'^api/(?P<venue_id>\d+)/customer_list/$', customer.customer_list,
        name='api_customer_list'),
    url(r'^api/user/(?P<user_id>\d+)/venue_list/$', venue.venue_list,
        name='api_venue_list'),
]