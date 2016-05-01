from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Venue, Menu, Item, Employee
from django.contrib.auth.models import User

def display(request, venue_id, employee_id):
    venue = Venue.objects.get(id=venue_id)
    items = Item.objects.all()
    employee = Employee.objects.get(id=employee_id)
    return render(request, "main/bartinterface.html", {'venue': venue, 'items': items, 'employee': employee})