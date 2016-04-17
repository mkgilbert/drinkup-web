from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from main.models import Order

def unclaimed(request):
    #creates list of objects
    orders = Order.objects.all()
    return render(request, 'main/unclaimed.html',{'unclaimed': orders })
