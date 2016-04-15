from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Customer, Venue
from main.serializers.customer import CustomerSerializer

@api_view(['GET',])
def customer_detail(request, cust_id):
    pass

@api_view(['GET', 'POST'])
def customer_list(request, venue_id):
    """
    List all customers in a venue or create a new one
    :param request:
    :return:
    """
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # get all customers for this venue
        customers = Customer.objects.all(filter=venue)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # add a new customer
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
