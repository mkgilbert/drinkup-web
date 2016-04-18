from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from main.models import Order, Venue, Employee

@login_required()
def unclaimed(request, venue_id):
    #creates list of objects
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        return HttpResponse(status=404)
    orders = venue.orders.filter(employee=None)
    employees = venue.employees.all()
    return render(request, 'main/unclaimed.html',{'venue': venue,
                                                  'orders': orders,
                                                  'employees': employees})
