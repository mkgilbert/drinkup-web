from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from main.models import Menu, Item, Venue, Customer, Order, ItemOrderLink, Employee
from main.serializers.order import OrderSerializer, CreateOrderElement
from main.serializers.employee import EmployeeSerializer

@api_view(['GET'])
def complete_item(request, venue_id, item_id):
    try:
        itemgotten = ItemOrderLink.objects.get(id=item_id)
    except ItemOrderLink.DoesNotExist:
        return Response({"invalid": "true"})

    if request.method == 'GET':
        itemgotten.status="complete"
        itemgotten.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# removes an item from a menu (for the venue owner only)
@api_view(['GET'])
def remove(request, venue_id, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response({"invalid": "true"})

    if request.method == 'GET':
        item.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# TODO: This view is for deleting order objects and really should move to api/order.py
@api_view(['GET'])
def delete_item(request, venue_id, item_id):
    try:
        itemgotten = ItemOrderLink.objects.get(id=item_id)
    except ItemOrderLink.DoesNotExist:
        return Response({"invalid": "true"})

    if request.method == 'GET':
        itemgotten.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)