from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Venue
from main.forms import AddVenueForm

def add(request, user_id):
    if request.method == 'POST':
        form = AddVenueForm(request.POST)
        if form.is_valid():
            new_venue = form.save(commit=False)
            new_venue.user = User.objects.get(pk=user_id)
            new_venue.save()
            # Venue.objects.create(
            #     user = User.objects.get(pk=user_id),
            #     phone = form.cleaned_data['phone'],
            #     name = form.cleaned_data['name'],
            #     address = form.cleaned_data['address'],
            #     description = form.cleaned_data['description'],
            #     website = form.cleaned_data['website'],
            #     hours = form.cleaned_data['hours'],
            #     service_type = form.cleaned_data['service_type']
            # )
            messages.success(request, "Venue successfully added")
            return HttpResponseRedirect('/user/home/' + str(user_id))
    elif request.method == 'GET':
        form = AddVenueForm()
    else:
        return HttpResponseRedirect('/user/add-venue/' + str(user_id))
    return render(request, 'main/venue_add.html', {'form': form})