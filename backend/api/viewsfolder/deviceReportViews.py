from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import DeviceReport,Devices
from ..serializers import deviceReportSerializer, deviceReportViewSerializer

class DeviceReportList(APIView):
    def get(self, request):
        devicereport = DeviceReport.objects.select_related('ps_no').all()
        serializer = deviceReportViewSerializer(devicereport, many=True)
        return Response(serializer.data)

def currentTime():
    curr_time = datetime.now(tz=None)
    return curr_time

def borrowOrReturn(request):
    print(request.path)
    if 'borrow' in request.path:
        print('bor')
        return 'bor'
    elif 'return' in request.path:
        print('ret')
        return 'ret'
        
class BorrowOrReturn(APIView):        
    def post(self, request):
        devUpdate = Devices.objects.get(assetNo = request.data['assetNo'])
        print('dev',devUpdate)       
        if devUpdate.assetAvailability== 'Available' and borrowOrReturn(request) == 'bor':                      
            serializer = deviceReportSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
            dtUp = DeviceReport.objects.filter(ps_no = request.data['ps_no'],assetNo=request.data['assetNo']).last()
            print(type(dtUp))
            dtUp.dateBorrowed = currentTime()
            dtUp.save()
            devUpdate.assetAvailability = 'Not Available'               
            devUpdate.save()      
            return Response('data is saved')
        elif devUpdate.assetAvailability== 'Not Available' and borrowOrReturn(request) == 'ret':
            print('inside return')
            dtUp = DeviceReport.objects.filter(ps_no = request.data['ps_no'], assetNo=request.data['assetNo']).last()
            dtUp.dateReturned = currentTime()
            devUpdate.assetAvailability = 'Available'
            dtUp.save()    
            devUpdate.save() 
            return Response('data is saved')
        elif devUpdate.assetAvailability== 'Available' and borrowOrReturn(request) == 'ret':
            return Response('you didnt borrow any device or you have entered wrong device number')           
        else:
            return Response('the device is not available')

class DeviceReturn(APIView):
    def get(self, request):      
        devicereports = DeviceReport.objects.filter(dateReturned__isnull =True)
        serializer = deviceReportViewSerializer(devicereports, many=True)
        return Response(serializer.data)