from django.db import models

class Todo(models.Model) :

    class Meta:
        ordering = ['-id']

    task = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.task

