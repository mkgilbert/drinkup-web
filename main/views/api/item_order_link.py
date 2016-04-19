from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Customer, Venue, Order, Item, ItemOrderLink
from main.serializers.order import ItemOrderLinkSerializer

@api_view(['GET', 'PATCH', 'DELETE'])
@csrf_exempt
def order_item(request, venue_id, link_id):
    try:
        link = ItemOrderLink.objects.get(pk=link_id)
    except ItemOrderLink.DoesNotExist:
        return Response({"invalid": "true"})

    if request.method == 'GET':
        serializer = ItemOrderLinkSerializer(link)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = ItemOrderLinkSerializer(link, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        link.delete()
        return Response(status=status.HTTP_200_OK)
    return Response({"invalid": "true"})

