from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Roaster, Calendar
from ..serializers import RoasterSerializer, CalendarSerializer
class RoasterPlan (APIView):
    def post(self, request):
        print(request.data)
        serializer = RoasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data)
    def get(self, request):
        roasters = Roaster.objects.all()
        serializer = RoasterSerializer(roasters, many=True)
        return Response(serializer.data)
 
class CalendarData(APIView):
    def post(self, request):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.is_valid())
    def get(self, request):
        dataa = Calendar.objects.all()
        serializer = CalendarSerializer(dataa, many=True)
        return Response(serializer.data)
    def delete(self, request):
        try:
            eventt = Calendar.objects.get(title= request.data['title'] , date = request.data['date'])
        except:
            return Response('Event doesnt exist')
        eventt.delete()
        return Response('Event deleted successfully', status=204)
class CalendarDropUpdate(APIView):
    def post(self, request):
        try:
            eventt = Calendar.objects.filter(title= request.data['title'] , date = request.data['olddate']).last()
        except:
            return Response('Data doesnt exist')
        eventt.end = request.data['end']
        eventt.date = request.data['date']
        eventt.save()
        return Response('Date is updated', status=200)
    
class CalendarUpdate(APIView):
    def post(self, request):
        print(request.data)
        try:
            eventt = Calendar.objects.filter(title= request.data['oldtitle'] , date = request.data['olddate']).last()
        except:
            return Response('Data doesnt exist')
        eventt.title = request.data['title']
        eventt.date = request.data['date']
        eventt.save()
        return Response('Date is updated', status=200)