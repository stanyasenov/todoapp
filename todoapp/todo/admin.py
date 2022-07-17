from django.contrib import admin

from todoapp.todo.models import Task


@admin.register(Task)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
