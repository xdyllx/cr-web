from django.urls import path
from task import views

app_name = 'task'

urlpatterns = [
    path('task', views.task_list, name='task_list'),
    path('add_task', views.add_task, name='add_task'),
    path('edit_task', views.edit_task, name='edit_task'),
    path('modify_task_status', views.modify_task_status, name='change_task_status'),
    # path('super', views.super_user, name='super'),
]