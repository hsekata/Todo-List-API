from django.contrib import admin

# Register your models here.
from .models import UserToDo, ToDos
admin.site.register(UserToDo)
admin.site.register(ToDos)
