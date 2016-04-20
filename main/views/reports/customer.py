from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Customer

@login_required()
def customer_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    customers = venue.customers.all()
    return render(request, "main/customer_report.html", {"venue": venue,
                                                         "customers": customers})
