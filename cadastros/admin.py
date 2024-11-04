from django.contrib import admin

# Register your models here.
from .models import User, Task, TaskList, Category, Auditable, Comment


admin.site.register(User)
admin.site.register(Task)
admin.site.register(TaskList)
admin.site.register(Category)
admin.site.register(Auditable)
admin.site.register(Comment)