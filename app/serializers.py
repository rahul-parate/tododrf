from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'

	def create(self):
		Task.objects.create(
			title=self.validated_data['title'],
			completed=self.validated_data['completed'],
			description=self.validated_data['description'],
			date_at=self.validated_data['date_at'],
			time=self.validated_data['time'])
		return True

	def update(self):
		Task.objects.filter(id=self.validated_data).update(
			title=self.validated_data['title'],
			completed=self.validated_data['completed'],
			description=self.validated_data['description'],
			date_at=self.validated_data['date_at'],
			time=self.validated_data['time']
			)
		return True

	def completed(self, taskid):
		task = Task.objects.filter(id=taskid)
		if task.completed:
			task.update(
				completed=False
				)
		else:
			task.update(
				completed=True
				)
		return True