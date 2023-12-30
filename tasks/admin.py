from django.contrib import admin
from .models import Task, TaskImage

class Task_admin(admin.ModelAdmin):
    list_display=('created_at', 'title', 'description', 'due_date','priority','status')

admin.site.register(Task, Task_admin)

class Taskimage_admin(admin.ModelAdmin):
    list_display=('size','image')
admin.site.register(TaskImage, Taskimage_admin)


