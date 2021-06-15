from django.db import models
from django.db.models import signals


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(
    	default=False, blank=True,null=True)
    description = models.CharField(max_length=500,null=True)
    is_deleted = models.BooleanField(default=False)
    date_at = models.DateField(blank=True, null=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
    	return self.title


class Notification(models.Model):

	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	is_viewed = models.BooleanField(default=False)


