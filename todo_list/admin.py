from django.contrib import admin
from todo_list.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "is_done")
    search_fields = ("content", )
    list_filter = ("tags", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name", )
