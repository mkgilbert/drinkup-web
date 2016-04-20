from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Employee

@login_required()
def employee_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    employees = venue.employees.all()
    return render(request, "main/employee_report.html", {"venue": venue,
                                                         "employees": employees,
                                                         "view_name": "reports_employees"})