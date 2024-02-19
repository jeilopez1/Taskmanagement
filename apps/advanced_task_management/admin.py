from django.contrib import admin
from .models import User, Task, Role, state_Task, Comment  

def register_models(*modelos):
    for modelo in modelos:
        class ModeloAdmin(admin.ModelAdmin):
            list_display = [field.name for field in modelo._meta.fields]

        admin.site.register(modelo, ModeloAdmin)

register_models(User, Task, Role, state_Task.stateTask, Comment)  # Añade todos tus modelos aquí
