
from rest_framework.response import Response
from .serializers import TaskSerializer, CreateTaskSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework import status
from .models import Task

class OverView(APIView):
	def get(self, request, *args, **kwargs):
		api_urls = {
			'List' : '/task-list/',
			'Detail View' : '/task-detail/<str:pk>/',
			'Create' : '/task-create/',
			'Update' : '/task-update/<str:pk>/',
			'Delete' : '/task-delete/<str:pk>/',
		}
		return Response(data=api_urls,status=status.HTTP_200_OK)


class CreateView(APIView):
	
	def post(self, request, *args, **kwargs):
		print(request.data)
		data = request.data
		res = None
		serializer = CreateTaskSerializer(data=data)
		if serializer.is_valid():
			print(serializer.data)
			res = serializer.create()
			print('res = ', res)
		return Response(data=res, status=status.HTTP_200_OK)



class EditView(APIView):
	def put(self, request, *args, **kwargs):
		print(request.data)
		data = request.data
		res = None
		
		if data.get('action' == 'update'):
			serializer = CreateTaskSerializer(data=data)
			if serializer.is_valid():
				print(serializer.data)
				res = serializer.update()
				print('res = ', res)
				return Response(data=res, status=status.HTTP_200_OK)
		else:
			task = Task.objects.filter(id=data.get('id')).first()
			if task.completed:
				task.completed=False
				
			else:
				task.completed=True
			task.save()
			return Response(data=res, status=status.HTTP_200_OK)
		return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteView(APIView):
	def delete(self, request, taskid, *args, **kwargs):
		print(request.data)
		task = Task.objects.filter(id=taskid).delete()
		return Response(data=True,status=status.HTTP_200_OK)


class DetailsView(APIView):
	def get(self, request, *args, **kwargs):
		api_urls = {
			'List' : '/task-list/',
			'Detail View' : '/task-detail/<str:pk>/',
			'Create' : '/task-create/',
			'Update' : '/task-update/<str:pk>/',
			'Delete' : '/task-delete/<str:pk>/',
		}
		return Response(data=api_urls,status=status.HTTP_200_OK)


class TaskList(APIView):
	
	def get(self, request ,*args, **kwargs):
		tasks = Task.objects.all()
		serializer = TaskSerializer(tasks, many = True)
		return Response(serializer.data)