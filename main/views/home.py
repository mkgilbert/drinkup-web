from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Menu, Employee, Item

@login_required()
def home(request):
    user = request.user
    venues = user.venues.all()
    menus = Menu.objects.all()
    employees = Employee.objects.all()
    items = Item.objects.all()
    return render(request, "main/home.html", {'user': user,
                                              'venue': "",
                                              'venues': venues,
                                              'menus': menus,
                                              'items':items,
                                              'employees': employees})
