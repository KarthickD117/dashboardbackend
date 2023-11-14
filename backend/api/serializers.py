from rest_framework import serializers
from .models import *

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