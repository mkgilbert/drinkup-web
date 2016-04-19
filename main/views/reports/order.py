from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def order_report(request, venue_id):
    pass