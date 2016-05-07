from django.conf.urls import url
from main.views.api import (customer, venue, menu, order, employee, item_order_link, item)

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
    url(r'^api/venue_remove/(?P<venue_id>\d+)/$', venue.remove,
        name='api_venue_remove'),
    # GET - list of all menus of a venue (not really going to be used probably)
    url(r'^api/(?P<venue_id>\d+)/menu_list/$', menu.menu_list,
        name='api_menu_list'),
    # GET - detailed menu info for a venue
    url(r'^api/(?P<venue_id>\d+)/menu_detail/$', menu.menu_detail,
        name='api_menu_detail'),
    url(r'^api/(?P<venue_id>\d+)/menu_remove/(?P<menu_id>\d+)/$', menu.remove,
        name='api_menu_remove'),
    url(r'^api/(?P<venue_id>\d+)/menu/remove_item/(?P<item_id>\d+)/$', item.remove,
    name='api_menu_item_remove'),
    # GET - detailed menu info
    url(r'^api/menu_listoff/(?P<menu_id>\d+)/$', menu.menu_listoff,
        name='api_menu_listoff'),
    # GET - all orders by a certain customer or POST a new order
    url(r'^api/(?P<venue_id>\d+)/order/(?P<cust_id>\d+)/$', order.order,
        name='api_order'),
    url(r'^api/(?P<venue_id>\d+)/employee_list/$', employee.employee_list,
        name='api_employee_list'),
    url(r'^api/(?P<venue_id>\d+)/employee_detail/(?P<cust_id>\d+)/$', employee.employee_detail,
        name='api_employee_detail'),
    url(r'^api/(?P<venue_id>\d+)/employee_remove/(?P<emp_id>\d+)/$', employee.remove,
        name='api_employee_remove'),
    url(r'^api/(?P<venue_id>\d+)/order_item/(?P<link_id>\d+)/$', item_order_link.order_item,
        name='api_order_item'),
    url(r'^api/(?P<venue_id>\d+)/complete_order/(?P<order_id>\d+)/$', order.complete_order,
        name='api_complete_order'),
    url(r'^api/(?P<venue_id>\d+)/complete_item/(?P<item_id>\d+)/$', item.complete_item,
        name='api_complete_item'),
    url(r'^api/(?P<venue_id>\d+)/delete_item/(?P<item_id>\d+)/$', item.delete_item,
        name='api_delete_item'),
    url(r'^api/(?P<venue_id>\d+)/order/(?P<cust_id>\d+)/pay$', order.pay,
        name='api_pay'),
]