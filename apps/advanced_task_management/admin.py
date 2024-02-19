from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps

class MiModeloAdmin(admin.ModelAdmin):
    app_models = apps.get_app_config('advanced_task_management').get_models()
    for model in app_models:
        admin.site.register(model)