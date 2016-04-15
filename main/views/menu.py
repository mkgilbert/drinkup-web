from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Venue, Menu, Item
from django.contrib.auth.models import User
from main.forms import AddMenuForm

def display(request, user_id, menu_id):
    user = User.objects.get(pk=user_id)
    menu = Menu.objects.get(id=menu_id)
    items = Item.objects.all()
    return render(request, "main/menu.html", {'user': user, 'menu': menu, 'items': items})

def add(request, user_id, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.method == 'POST':
        form = AddMenuForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.venue = venue
            new_item.save()
            messages.success(request, "Menu successfully added")
            return HttpResponseRedirect('/user/home/' + str(venue.user.id) + '/')
    elif request.method == 'GET':
        form = AddMenuForm()
    else:
        return HttpResponseRedirect('/user/home/' + str(venue.user.id) + '/' + str(venue.id) + '/add-menu/')
    return render(request, 'main/menu_add.html', {'form': form})