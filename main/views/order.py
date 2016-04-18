from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from main.models import Order


def order(request):
    orders = Order.objects.all()
    items = {}
    for ord in orders:
        items[ord.id] = ord.items.all()
    return render(request, 'order.html',{'orders': orders, 'items':items})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
