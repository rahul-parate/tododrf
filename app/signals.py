from .tasks import add_reminder, add
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Task

@receiver(post_save, sender=Task)
def create_task(sender, instance, **kwargs):
    add_reminder.delay(id=str(instance.id))
    return