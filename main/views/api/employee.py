from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Venue, Employee
from main.serializers.employee import EmployeeSerializer

@api_view(['GET'])
def employee_detail(request, venue_id, emp_id):
    """
    Get a specific employee's information
    :param request:
    :param venue_id:
    :param emp_id:
    :return:
    """
    try:
        venue = Venue.objects.get(pk=venue_id)
        employee = venue.employees.get(pk=emp_id)
    except Employee.DoesNotExist or Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


@api_view(['GET'])
def employee_list(request, emp_id):
    """
    List all employees in a venue
    :param request:
    :return:
    """
    try:
        venue = Venue.employees.get(pk=emp_id)
    except Employee.DoesNotExist or Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # get all customers for this venue
        employees = venue.employees.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

