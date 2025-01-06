from django.contrib import admin

# Register your models here.
from .models import Task
from django.contrib.auth.models import User

admin.site.register(Task)
# admin.site.register(User)
