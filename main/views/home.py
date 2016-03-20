from django.shortcuts import render
from main.models import Business

def home(request):
    all_businesses = Business.objects.all()
    return render(request, "main/home.html", {'businesses': all_businesses})
