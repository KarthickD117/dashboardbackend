from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"

class deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = "__all__"

class deviceReportViewSerializer(serializers.ModelSerializer):
    ps_no = EmployeeSerializer()
    assetNo = deviceSerializer()
    class Meta:
        model = DeviceReport
        fields = ('id','ps_no','assetNo','dateBorrowed','dateReturned')

class deviceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceReport
        fields = ('id','ps_no','assetNo','dateBorrowed','dateReturned')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'username': self.user.username}) # type: ignore
        data.update({'firstname': self.user.first_name}) # type: ignore
        data.update({'isSuperUser': self.user.is_superuser}) # type: ignore
        data.update({'isAdmin':self.user.is_staff})
        return data