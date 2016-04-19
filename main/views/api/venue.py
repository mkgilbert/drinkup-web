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
def venue_detail(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"invalid": "true"})
    serializer = VenueSerializer(venue)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def venue_list(request):
    venues = Venue.objects.all()
    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
