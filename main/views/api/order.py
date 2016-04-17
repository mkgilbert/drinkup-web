from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Menu, Item, Venue, Customer, Order, ItemOrderLink
from main.serializers.menu import MenuSerializer, ItemSerializer
from main.serializers.order import OrderSerializer, ItemOrderLinkSerializer, CreateOrderElement

@api_view(['GET',])
def order_detail(request, venue_id, order_id):
    """
    show a specific order
    """
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def order(request, venue_id, cust_id):
    """
    Get or create a new order
    """
    if request.method == 'GET':
        try:
            customer = Customer.objects.get(pk=cust_id)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        orders = customer.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        try:
            venue = Venue.objects.get(pk=venue_id)
            customer = Customer.objects.get(pk=cust_id)

        except Venue.DoesNotExist or Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.create(venue=venue, customer=customer)
        #items = request.POST.get('items')

        serializer = CreateOrderElement(data=request.data, many=True, order=order)
        #serializer = OrderSerializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
        # items = [{"item_id": 1, "item_qty": 1}, {"item_id": 3, "item_qty": 1}]
        # if items is None or len(items) == 0:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        #
        # for item in items:
        #     try:
        #         item_obj = Item.objects.get(pk=int(item['item_id']))
        #         order.add_item(item_obj, int(item['item_qty']))
        #     except Item.DoesNotExist:
        #         return Response(status=status.HTTP_404_NOT_FOUND)
        #
        # return Response(status=status.HTTP_201_CREATED)
