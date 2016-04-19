from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from main.models import Menu, Item, Venue, Customer, Order, ItemOrderLink, Employee
from main.serializers.order import OrderSerializer, CreateOrderElement
from main.serializers.employee import EmployeeSerializer

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

@api_view(['GET', 'POST','PATCH'])
#@permission_classes((AllowAny, ))
def order(request, venue_id, cust_id):
    """
    Get or create a new order
    """
    if request.method == 'GET':
        if cust_id == "0":
            venue = Venue.objects.get(pk=venue_id)
            orders = venue.orders.all()
        else:
            try:
                customer = Customer.objects.get(pk=cust_id)
            except Customer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            orders = customer.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        print(request.data)
        try:
            order_id = request.data.pop('order_id')
            order = Order.objects.get(pk=order_id)
            if request.data.get('employee'):
                emp_info = request.data.get('employee')
                employee = Employee.objects.get(pk=emp_info['id'])
                order.employee = employee
                order.save()
                return Response(status=status.HTTP_200_OK)
            #print(emp_name)
            #request.data['employee'] = {'name': emp_name}
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        #print(request.data.get('employee'))
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        print("venue: " + str(venue_id))
        print("customer: " + str(cust_id))
        try:
            venue = Venue.objects.get(pk=venue_id)
            print(venue)
            customer = Customer.objects.get(pk=cust_id)
            print(customer)
        except Venue.DoesNotExist or Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.create(venue=venue, customer=customer)

        serializer = CreateOrderElement(data=request.data, many=True, order=order)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET'])
def complete_order(request, venue_id, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response({"invalid": "true"})

    if request.method == 'GET':
        order.complete_all_items()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)