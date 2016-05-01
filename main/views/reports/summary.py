from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Venue, Customer, Order, Employee
from datetime import timezone
import datetime

@login_required()
def summary_report(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    customers = venue.customers.all()
    orders = venue.orders.all()
    total_sold = 0
    min_time_in_secs = -1
    for order in orders:
        total_sold += order.get_num_items()
        time = order.get_time_to_complete
        if time is not None:
            if min_time_in_secs == -1:
                min_time_in_secs = time
                continue
            if time < min_time_in_secs:
                min_time_in_secs = time
    time = ""
    if min_time_in_secs != -1:
        mins = min_time_in_secs // 60
        secs = min_time_in_secs % 60
        time += str(mins) + " mins, " + str(secs) + " secs"
    else:
        time += "N/A"

    time_in_biz = datetime.datetime.now(timezone.utc) - request.user.date_joined
    time_in_biz = time_in_biz - datetime.timedelta(microseconds=time_in_biz.microseconds)
    employees = venue.employees.all()
    return render(request, "main/summary_report.html", {"venue": venue,
                                                        "customers": customers,
                                                        "orders": orders,
                                                        "total_sold": total_sold,
                                                        "time": time,
                                                        "time_in_biz": time_in_biz,
                                                        "employees": employees,
                                                        "view_name": "reports_summary"})