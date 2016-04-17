from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Venue
from main.forms import AddVenueForm

@login_required()
def add(request):
    if request.method == 'POST':
        form = AddVenueForm(request.POST)
        if form.is_valid():
            new_venue = form.save(commit=False)
            new_venue.user = User.objects.get(pk=request.user.id)
            new_venue.save()
            messages.success(request, "Venue successfully added")
            return HttpResponseRedirect('/user/home/')
    elif request.method == 'GET':
        form = AddVenueForm()
    else:
        return HttpResponseRedirect('/user/add-venue/')
    return render(request, 'main/venue_add.html', {'form': form})

@login_required()
def edit(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.method == 'POST':
        form = AddVenueForm(request.POST, instance=venue)
        if form.is_valid():
            new_venue = form.save(commit=False)
            new_venue.save()
            messages.success(request, "Venue successfully updated")
            return HttpResponseRedirect('/user/home')
    elif request.method == 'GET':
        form = AddVenueForm(instance=venue)
    else:
        return HttpResponseRedirect('/user/home/' + str(venue.id) + '/edit-venue/')
    return render(request, 'main/venue_edit.html', {'form': form})