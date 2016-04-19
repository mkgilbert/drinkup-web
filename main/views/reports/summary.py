from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Customer, Order, Employee

@login_required()
def summary_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    customers = venue.customers.all()
    orders = venue.orders.all()
    employees = venue.employees.all()
    return render(request, "main/summary_report.html", {"venue": venue,
                                                                  "customers": customers,
                                                                  "orders": orders,
                                                                  "employees": employees})