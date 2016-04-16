from django.conf.urls import url
from main.views.api import (customer, venue, menu)

urlpatterns = [
    url(r'^api/(?P<venue_id>\d+)/customer_list/$', customer.customer_list,
        name='api_customer_list'),
    url(r'^api/(?P<venue_id>\d+)/customer_detail/(?P<cust_id>\d+)/$', customer.customer_detail,
        name='api_customer_detail'),
    url(r'^api/user/(?P<user_id>\d+)/venue_list/$', venue.venue_list,
        name='api_venue_list'),
    url(r'^api/(?P<venue_id>\d+)/menu_list/$', menu.menu_list,
        name='api_menu_list'),
    url(r'^api/(?P<venue_id>\d+)/menu_detail/$', menu.menu_detail,
        name='api_menu_detail'),


]