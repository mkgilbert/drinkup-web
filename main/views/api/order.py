from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from main.models import Menu, Item, Venue, Customer, Order, ItemOrderLink, Employee
from main.serializers.order import OrderSerializer, CreateOrderElement
from main.serializers.employee import EmployeeSerializer
from datetime import datetime

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
        # the case where the web app is trying to populate the entire bar interface page
        # just chose to use "0" because it's a non-existent customer id
        if cust_id == "0":
            venue = Venue.objects.get(pk=venue_id)
            # only get orders that have items in them
            orders = venue.orders.filter(items__isnull=False)
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
            if request.data.get('pin'):
                emp_pin = request.data.get('pin')
                try:
                    employee = Employee.objects.get(pin=emp_pin)
                except Employee.DoesNotExist:
                    return Response({"invalid": "true", "message": "employee does not exist with that pin"})
                order.time_completed = datetime.now()
                order.employee = employee
                order.is_delivered = True
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
        try:
            venue = Venue.objects.get(pk=venue_id)
            print("venue: " + str(venue))
            customer = Customer.objects.get(pk=cust_id)
            print("customer: " + str(customer))
        except Venue.DoesNotExist or Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.create(venue=venue, customer=customer)
        print("order was successfully created...")
        serializer = CreateOrderElement(data=request.data, many=True, order=order)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            print("serializer was validated")
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
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

@api_view(['POST'])
def pay(request, venue_id, cust_id):
    result = {}
    if request.data['pay'] is not None:
        if request.data['pay'] == True:
            try:
                customer = Customer.objects.get(pk=cust_id)
                print("pay all for customer " + customer.name)
                orders = customer.orders.all()
                if orders is not None:
                    for order in orders:
                        order.is_paid = True
                        order.save()
                result["status"] = "paid all"
            except Customer.DoesNotExist:
                result['invalid'] = "true"
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response({"invalid": "true"})
    return Response()
