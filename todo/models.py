from django.db import models

# Create your models here.

# Todo 
#     id = models.IntegerField
#     title: string
#     is_complete: boolean

class Todo(models.Model):
    title = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title