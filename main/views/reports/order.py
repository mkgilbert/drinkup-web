from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Order

@login_required()
def order_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    all_orders = Order.objects.filter(venue=venue).order_by('is_delivered')
    orders = []
    for i in range(len(all_orders)):
        if all_orders[i].get_num_items() == 0:
            continue
        orders.append(all_orders[i])

    return render(request, 'main/order_report.html', {"orders": orders})