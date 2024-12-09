from django.contrib import admin
from .models import Task, Category, Auditable, Comment

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Auditable)
admin.site.register(Comment)