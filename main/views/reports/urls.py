from django.conf.urls import url
from main.views.reports import (customer, employee, order, summary, item)

urlpatterns = [
    url(r'^user/home/venue/(?P<venue_id>\d+)/reports/summary', summary.summary_report, name='summary_report'),

    url(r'^user/home/venue/(?P<venue_id>\d+)/reports/items', item.item_report, name='item_report'),

]