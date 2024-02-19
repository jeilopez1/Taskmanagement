from django.db import models
from .User import User
from .state_Task import stateTask

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    id_stateTask = models.ForeignKey(stateTask, on_delete=models.CASCADE, related_name='estado_tarea')
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_asignadas')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo