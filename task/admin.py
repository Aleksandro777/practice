from django.contrib import admin
from django.core.checks import Tags

from task.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created")


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name",)
