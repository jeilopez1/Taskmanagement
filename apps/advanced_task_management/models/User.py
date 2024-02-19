from django.db import models
from .Role import Role

class User(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre