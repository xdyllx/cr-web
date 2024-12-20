from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from task.models import Task
from task.serializers import TaskListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def task_list(request):
    print(request.user, request.user.username)
    tasks = Task.objects.all()
    serializer = TaskListSerializer(tasks, many=True)
    print(type(serializer.data), serializer.data)
    print(request.user)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_task(request):
    serializer = TaskListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data)


@api_view(['GET'])
def super_user(request):
    print(request.user, type(request.user))
    print(request.user.is_superuser)
    user = request.user
    print(user.username)
    print(user.password)
    # user.is_superuser = True
    # user.save()
    return JsonResponse({}, safe=False)
