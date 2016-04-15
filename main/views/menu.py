from django.shortcuts import render
from main.models import Venue, Menu, Item
from django.contrib.auth.models import User

def menu(request, user_id, menu_id):
    user = User.objects.get(pk=user_id)
    menu = Menu.objects.get(id=menu_id)
    items = Item.objects.all()
    return render(request, "main/menu.html", {'user': user, 'menu': menu, 'items': items})
