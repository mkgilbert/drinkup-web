from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/home/')
            else:
                messages.error(request, 'Incorrect username or password')
                return HttpResponseRedirect('/login/')
    elif request.method == 'GET':
        form = LoginForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def user_edit(request):
    user = request.user
    venue = user.venues.first()
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            messages.success(request, "Account successfully updated")
            return HttpResponseRedirect('/user/home/')
    elif request.method == 'GET':
        form = UserCreationForm(instance=user)
    else:
        return HttpResponseRedirect('/user/home/edit-user/')
    return render(request, 'main/user_edit.html', {'form': form, 'venue': venue})

@login_required()
def user_delete(request):
    user = request.user
    user.delete()
    return HttpResponseRedirect('/')