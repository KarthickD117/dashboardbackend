from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Devices
from ..serializers import EmployeeSerializer, deviceSerializer

class DeviceList(APIView):
    def get(self, request):
        device = Devices.objects.all()
        serializer = deviceSerializer(device, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = deviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class DeviceDetail(APIView):
    def get(self, request, AssetNo):
        try:
            device = Devices.objects.get(assetNo=AssetNo)
            serializer = deviceSerializer(device)
            return Response(serializer.data)
        except Devices.DoesNotExist:
            return Response({'error': 'device not found'}, status=404)

    def put(self, request, AssetNo):
        try:
            device = Devices.objects.get(assetNo=AssetNo)
        except Devices.DoesNotExist:
            return Response({'error': 'device not found'}, status=404)

        serializer = deviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, AssetNo):
        try:
            device = Devices.objects.get(assetNo=AssetNo)
        except Devices.DoesNotExist:
            return Response({'error': 'device not found'}, status=404)
        device.delete()
        return Response(status=204)
