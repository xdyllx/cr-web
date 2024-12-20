from django.urls import path
from task import views

app_name = 'task'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('super', views.super_user, name='super'),
]