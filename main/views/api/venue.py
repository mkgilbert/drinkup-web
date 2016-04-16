from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Customer, Venue
from main.serializers.customer import CustomerSerializer
from main.serializers.venue import VenueSerializer
from django.contrib.auth.models import User

@api_view(['GET',])
def venue_detail(request):
    serializer = VenueSerializer(data=request.data)
    return Response(serializer.data)

@api_view(['GET'])
def venue_list(request, user_id):
    try:
        user= User.objects.get(pk=user_id)
        venues = Venue.objects.filter(user=user)
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data, status=200)
