from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Menu, Item, Venue
from main.serializers.menu import MenuSerializer, ItemSerializer

@api_view(['GET',])
def menu_detail(request, venue_id):
    """
    Show all the items in a single menu
    :param request:
    :param venue_id:
    :return:
    """
    try:
        venue = Venue.objects.get(pk=venue_id)
        # TODO: allow multiple menus...also figure out which one "get" gets
        menu = venue.menus.filter().first()
    except Menu.DoesNotExist or Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MenuSerializer(menu)
    return Response(serializer.data)

@api_view(['GET',])
def menu_listoff(request, menu_id):
    """
    Show all the items in a single menu
    :param request:
    :param venue_id:
    :return:
    """
    try:
        menu = Menu.objects.get(pk=menu_id)
        venue = Venue.objects.get(pk=menu.venue.id)
        # TODO: allow multiple menus...also figure out which one "get" gets
    except Menu.DoesNotExist or Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MenuSerializer(menu)
    return Response(serializer.data)

@api_view(['GET'])
def menu_list(request, venue_id):
    """
    Show a list of all the menus of a single venue. This really isn't useful for
    our purposes right now, as we're only using 1 menu
    :param request:
    :param venue_id:
    :return:
    """
    try:
        venue = Venue.objects.get(pk=venue_id)
        menus = venue.menus.all()
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
