from django.db import models
from .Task import Task
from .User import User

class Comment(models.Model):
    contenido = models.TextField()
    tarea = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.contenido