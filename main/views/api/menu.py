from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Menu, Item, Venue
from main.serializers.menu import MenuSerializer, ItemSerializer
from django.contrib.auth.models import User

@api_view(['GET',])
def menu_detail(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
        # TODO: allow multiple menus...also figure out which one "get" gets
        menu = venue.menus.get(pk=1)
        items = menu.items.all()
    except Menu.DoesNotExist or Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def menu_list(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
        menus = venue.menus.all()
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
