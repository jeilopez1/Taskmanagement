from django.db import models

class Role(models.Model):
    nombre = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre