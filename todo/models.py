from django.db import models
import uuid
# Create your models here.


class Todo(models.Model):
    id = models.UUIDField(editable=False, unique=True,
                          default=uuid.uuid4, primary_key=True)
    task = models.TextField(max_length=1000, blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task}"
