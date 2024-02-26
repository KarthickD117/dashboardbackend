from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Tasks
from ..serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
import json
class TasksView(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Task saved successfully')
        else:
            return Response("An error Occured",status=400)
class TasksUpdate(APIView):
    def post(self, request):
        try:
            tasks = Tasks.objects.get(ReleaseName = request.data['ReleaseName'])
        except:
            return Response("Task Doesnt exist")
        try:
            tasks.Comment = json.loads(request.data['Comment'])
            tasks.CurrentCount = json.loads(request.data['CurrentCount'])
        except:
            tasks.Comment = (request.data['Comment'])
            tasks.CurrentCount = request.data['CurrentCount']
        tasks.Category = request.data['Category']
        tasks.TestRail = request.data['TestRail']
        tasks.TestRaidId = request.data['TestRaidId']
        tasks.Build = request.data['Build']
        tasks.DefectLink =request.data['DefectLink']
        tasks.TotalTC = request.data['TotalTC']
        
        tasks.Poc = request.data['Poc']
        tasks.Status =request.data['Status']
        tasks.save()
        return Response('Tasks saved successfully', status=200)
    def delete(self, request):
        try:
            tasks = Tasks.objects.get(ReleaseName = request.data['ReleaseName'])
        except:
            return Response('Tasks doesnt exist')
        tasks.delete()
        return Response('Tasks deleted successfully', status=204)