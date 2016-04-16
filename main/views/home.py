from django.shortcuts import render
from main.models import Venue, Menu
from django.contrib.auth.models import User

def home(request, user_id):
    user = User.objects.get(pk=user_id)
    venues = user.venues.all()
    menus = Menu.objects.all()
    return render(request, "main/home.html", {'user': user, 'venues': venues, 'menus': menus})
