from django.db import models

class stateTask(models.Model):
    state_task = models.CharField(max_length=200)
    descripcion = models.TextField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.state_task