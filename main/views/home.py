from django.shortcuts import render
from main.models import Business
from django.contrib.auth.models import User

def home(request, user_id):
    user = User.objects.get(pk=user_id)
    business = Business.objects.get(user=user)
    return render(request, "main/home.html", {'user': user, 'business': business})
