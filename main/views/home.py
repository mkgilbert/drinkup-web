from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Menu, Employee

@login_required()
def home(request):
    user = request.user
    venues = user.venues.all()
    venue = venues[0]
    menus = Menu.objects.all()
    employees = Employee.objects.all()
    return render(request, "main/home.html", {'user': user,
                                              'venue': venue,
                                              'venues': venues,
                                              'menus': menus,
                                              'employees': employees})
