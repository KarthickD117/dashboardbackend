from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Employees
from ..serializers import EmployeeSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Group

class EmployeeList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.has_perm('api.view_employees'):
            employee = Employees.objects.all().order_by('Firstname')
            serializer = EmployeeSerializer(employee, many=True)
            return Response({'data':serializer.data, 'perm':request.user.has_perm('api.add_employees')})
        else:
            return Response('User does not have permission', status=403)

    def post(self, request):
        if request.user.has_perm('api.add_employees'):
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('User added successfully', status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response('User does not have permission',status=403)
    
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
        return Response('user deleted successfully',status=204)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()



#class Createuser (APIView):
#    def post(self, request):
#        user = User.objects.create_user(username=request.data['username'], password=request.data['password'], email=request.data['email'] )
#        user.first_name=request.data['firstname']
#        user.last_name=request.data['lastname']
#        group = Group.objects.get(name="users group")
#        user.groups.add(group)
#        user.save()
#        return Response('user is created')
            
