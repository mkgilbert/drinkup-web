from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Venue, Menu, Item
from django.contrib.auth.models import User

def display(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    items = Item.objects.all()
    return render(request, "main/test.html", {'venue': venue, 'items': items})