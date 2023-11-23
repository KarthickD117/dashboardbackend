from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import DeviceReport,Devices
from ..serializers import deviceReportSerializer, deviceReportViewSerializer
from rest_framework.permissions import IsAuthenticated


class DeviceReportList(APIView):
    def get(self, request):
        devicereport = DeviceReport.objects.select_related('ps_no').all()
        serializer = deviceReportViewSerializer(devicereport, many=True)
        return Response(serializer.data)

def currentTime():
    curr_time = datetime.now(tz=None).replace(microsecond=0)
    return curr_time

def borrowOrReturn(request):
    print(request.path)
    if 'borrow' in request.path:
        return 'bor'
    elif 'return' in request.path:
        return 'ret'
        
class BorrowOrReturn(APIView):
    permission_classes = [IsAuthenticated]        
    def post(self, request):
        devUpdate = Devices.objects.get(assetNo = request.data['assetNo'])    
        if devUpdate.assetAvailability== 'Available' and borrowOrReturn(request) == 'bor':                      
            serializer = deviceReportSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
            dtUp = DeviceReport.objects.filter(ps_no = request.data['ps_no'],assetNo=request.data['assetNo']).last()
            dtUp.dateBorrowed = currentTime()
            dtUp.save()
            devUpdate.assetAvailability = 'Not Available'               
            devUpdate.save()      
            return Response('data is saved')
        elif devUpdate.assetAvailability== 'Not Available' and borrowOrReturn(request) == 'ret':
            dtUp = DeviceReport.objects.filter(ps_no = request.data['ps_no'], assetNo=request.data['assetNo']).last()
            dtUp.dateReturned = currentTime()
            devUpdate.assetAvailability = 'Available'
            dtUp.save()    
            devUpdate.save() 
            return Response('data is saved')
        elif devUpdate.assetAvailability== 'Available' and borrowOrReturn(request) == 'ret':
            return Response('You didnt borrow any device or you have entered wrong device number')           
        else:
            return Response('The device is not available')

class DeviceReturn(APIView):
    def get(self, request):      
        devicereports = DeviceReport.objects.filter(dateReturned__isnull =True)
        serializer = deviceReportViewSerializer(devicereports, many=True)
        return Response(serializer.data)
