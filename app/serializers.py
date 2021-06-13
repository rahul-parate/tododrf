from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CreateTaskSerializer(serializers.Serializer):

	title = serializers.CharField(
		max_length=200, allow_null=True, allow_blank=True)
	completed = serializers.BooleanField()
	description = serializers.CharField(
		max_length=500, allow_blank=True, allow_null=True)

	def create(self):
		Task.objects.create(
			title=self.validated_data['title'],
			completed=self.validated_data['completed'],
			description=self.validated_data['description'])
		return True

	def update(self):
		Task.objects.filter(id=self.validated_data).update(
			title=self.validated_data['title'],
			completed=self.validated_data['completed'],
			description=self.validated_data['description']
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