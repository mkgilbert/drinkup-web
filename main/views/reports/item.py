from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Item, Order, ItemOrderLink

@login_required()
def item_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    menus = [{"name": "menu1",
              "items": [{"name": "drink1",
                         "total": 5},
                        {"name": "drink2",
                         "total": 3}]}]
    #for menu in venue.menus:
    #    menus.append({"menu": {menu)
    links = ItemOrderLink.objects.filter(order__venue_id=venue_id).order_by('item_id')

    items_info = {}
    for item in Item.objects.filter(menu__venue__id=venue_id).order_by('id'):
        items_info[item] = 0

    for link in links:
        items_info[link.item] += 1

    return render(request, "main/item_report.html", {"items_info": items_info})
