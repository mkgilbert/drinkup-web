from django.shortcuts import render

def index(request):
    if request.user.is_authenticated():
        user_is_logged_in = True
        venue = request.user.venues.first()
    else:
        user_is_logged_in = False
        venue = ""

    return render(request, 'index.html', { 'user': request.user,
                                           'user_is_logged_in': user_is_logged_in,
                                           'venue': venue} )