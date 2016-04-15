from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Item, Menu
from main.forms import AddItemForm

def add(request, user_id, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.menu = menu
            new_item.save()
            messages.success(request, "Item successfully added")
            return HttpResponseRedirect('/user/home/' + str(menu.venue.user.id) + '/menu/' + str(menu.id) + '/')
    elif request.method == 'GET':
        form = AddItemForm()
    else:
        return HttpResponseRedirect('/user/home/' + str(menu.venue.user.id) + '/menu/' + str(menu.id) + '/add-item')
    return render(request, 'main/item_add.html', {'form': form})