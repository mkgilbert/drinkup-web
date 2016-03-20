from django.shortcuts import render
from main.models import Venue
from django.contrib.auth.models import User

def home(request, user_id):
    user = User.objects.get(pk=user_id)
    venues = user.venue_set.all()
    return render(request, "main/home.html", {'user': user, 'businesses': venues})
