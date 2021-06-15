from celery import Celery
from todo_project.celery import celeryapp
from .models import Task, Notification

@celeryapp.task
def add(x, y):
	return x + y

@celeryapp.task
def add_reminder(**kwargs):
	try:
		task_id = kwargs.get("id")
		task = Task.objects.get(id= int(task_id))
		Notification.objects.create(
			task=task)
	except Exception as e:
		print(e)


