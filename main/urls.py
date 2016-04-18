from django.conf.urls import url
from main.views.api import (customer, venue, menu, order, employee)

urlpatterns = [
    # GET all customers for a venue or POST a new customer for a venue
    url(r'^api/(?P<venue_id>\d+)/customer_list/$', customer.customer_list,
        name='api_customer_list'),
    # GET - customer info
    url(r'^api/(?P<venue_id>\d+)/customer_detail/(?P<cust_id>\d+)/$', customer.customer_detail,
        name='api_customer_detail'),
    # GET - list all venues in the system
    url(r'^api/venue_list/$', venue.venue_list,
        name='api_venue_list'),
    # GET - detailed venue info on one venue
    url(r'^api/venue_detail/(?P<venue_id>\d+)/$', venue.venue_detail,
        name='api_venue_detail'),
    # GET - list of all menus of a venue (not really going to be used probably)
    url(r'^api/(?P<venue_id>\d+)/menu_list/$', menu.menu_list,
        name='api_menu_list'),
    # GET - detailed menu info for a venue
    url(r'^api/(?P<venue_id>\d+)/menu_detail/$', menu.menu_detail,
        name='api_menu_detail'),
    # GET - all orders by a certain customer or POST a new order
    url(r'^api/(?P<venue_id>\d+)/order/(?P<cust_id>\d+)/$', order.order,
        name='api_order'),
    url(r'^api/(?P<venue_id>\d+)/employee_list/$', employee.employee_list,
        name='api_order'),
    url(r'^api/(?P<venue_id>\d+)/employee_detail/(?P<cust_id>\d+)/$', employee.employee_detail,
        name='api_order'),
]