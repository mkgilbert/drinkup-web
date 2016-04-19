from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Employees

@login_required()
def customer_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    employees = venue.employees.all()
    return render(request, "main/employee_report.html", {"venue": venue,
                                                                  "customers": employees})