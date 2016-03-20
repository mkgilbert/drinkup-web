from django.shortcuts import render

def success(request):
    return render(request, 'register_success.html')