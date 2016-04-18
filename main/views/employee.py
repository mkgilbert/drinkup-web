from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Venue, Employee
from django.contrib.auth.models import User
from main.forms import AddEmployeeForm

@login_required()
def add(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.venue = venue
            new_item.save()
            messages.success(request, "Employee successfully added")
            return HttpResponseRedirect('/user/home/')
    elif request.method == 'GET':
        form = AddEmployeeForm()
    else:
        return HttpResponseRedirect('/user/home/' + str(venue.id) + '/add-employee/')
    return render(request, 'main/employee_add.html', {'form': form, "venue": venue})

@login_required()
def edit(request, venue_id, employee_id):
    venue = Venue.objects.get(pk=venue_id)
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            messages.success(request, "Employee successfully updated")
            return HttpResponseRedirect('/user/home/')
    elif request.method == 'GET':
        form = AddEmployeeForm(instance=employee)
    else:
        return HttpResponseRedirect('/user/home/' + str(employee.venue.id) + '/employee/' + str(employee.id) + '/edit-employee/')
    return render(request, 'main/employee_edit.html', {'form': form, "venue": venue})