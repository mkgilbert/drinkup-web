from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from main.models import Venue, Menu, Employee, Item

@login_required()
def home(request):
    user = request.user
    venues = user.venues.all()
    menus = Menu.objects.all()
    employees = Employee.objects.all()
    items = Item.objects.all()
    cost = {}
    for item in items:
        cost[item.id] = ("{:,.2f}".format(item.price))
    return render(request, "main/home.html", {'user': user,
                                              'venue': "",
                                              'venues': venues,
                                              'menus': menus,
                                              'items':items,
                                              'employees': employees,
                                              "cost":cost})
#ability to look up dictionary values
#used for looking up price
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
