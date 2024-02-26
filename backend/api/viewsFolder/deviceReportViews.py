from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import DeviceReport,Devices
from ..serializers import deviceReportSerializer, deviceReportViewSerializer
from rest_framework.permissions import IsAuthenticated

def currentTime():
    curr_time = datetime.now(tz=None).replace(microsecond=0)
    return curr_time

def borrowOrReturn(request):
    print(request.path)
    if 'borrow' in request.path:
        return 'bor'
    elif 'return' in request.path:
        return 'ret'

def convertStringtoDate(dateString):
    if len(dateString) == 10:
        format = '%Y-%m-%d'
    else:
        format = '%Y-%m'
    return datetime.strptime(dateString, format)

class DeviceReportList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.has_perm('api.view_devicereport'):
            devicereport = DeviceReport.objects.select_related('ps_no').all().order_by('-id')
            serializer = deviceReportViewSerializer(devicereport, many=True)
            return Response(serializer.data)
        else:
            return Response('The user doesnot have access', status=403)

class BorrowOrReturn(APIView):
    permission_classes = [IsAuthenticated]        
    def post(self, request):
        if request.user.has_perm('api.add_devicereport'):
            devUpdate = Devices.objects.get(assetNo = request.data['assetNo'])     
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
                dtUp = DeviceReport.objects.filter(ps_no = request.data['ps_no'], assetNo=request.data['assetNo']).last()
                dtUp.dateReturned = currentTime()
                devUpdate.assetAvailability = 'Available'
                dtUp.save()    
                devUpdate.save() 
                return Response('data is saved')
            elif devUpdate.assetAvailability== 'Available' and borrowOrReturn(request) == 'ret':
                return Response('you didnt borrow any device or you have entered wrong device number')           
            else:
                return Response('The device is not available at the moment please try again later', status=503)
        else:
            return Response('The user doesnot have access', status=403)

class DeviceReturn(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.has_perm('api.view_devicereport'):
            if request.user.is_staff:     
                devicereports = DeviceReport.objects.filter(dateReturned__isnull =True).order_by('id')
                serializer = deviceReportViewSerializer(devicereports, many=True)
                return Response(serializer.data)
            else:
                devicereports = DeviceReport.objects.filter(dateReturned__isnull =True, ps_no = request.user.username).order_by('id')
                serializer = deviceReportViewSerializer(devicereports, many=True)
                return Response(serializer.data)
        else:
            return Response('The user doesnot have access', status=403)
    
class FilterDate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        if request.user.has_perm('api.view_devicereport'):
            dateobj = convertStringtoDate(pk)
            if len(pk) == 10:
                devicerp = DeviceReport.objects.filter(dateBorrowed__date = dateobj.date(), dateBorrowed__month = dateobj.month, dateBorrowed__year = dateobj.year).order_by('id')
            else:
                devicerp = DeviceReport.objects.filter(dateBorrowed__month = dateobj.month, dateBorrowed__year = dateobj.year).order_by('id')
            serializer = deviceReportViewSerializer(devicerp, many=True)
            return Response(serializer.data)
        else:
            return Response('The user doesnot have permission',status=403)
