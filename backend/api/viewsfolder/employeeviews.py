from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Employees
from ..serializers import EmployeeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print('authication', request.user)
        employee = Employees.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class EmployeeDetail(APIView):
    def get(self, request, ps_no):
        try:
            employee = Employees.objects.get(ps_no=ps_no)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employees.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=404)

    def put(self, request, ps_no):
        try:
            employee = Employees.objects.get(ps_no=ps_no)
        except Employees.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=404)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, ps_no):
        try:
            employee = Employees.objects.get(ps_no=ps_no)
        except Employees.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=404)
        employee.delete()
        return Response(status=204)
