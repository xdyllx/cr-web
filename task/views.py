from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse

from task.models import Task
from task.serializers import TaskListSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from django.utils import timezone
from task.permission import CsrfExemptSessionAuthentication


def get_all_task_info():
    tasks = Task.objects.all()
    serializer = TaskListSerializer(tasks, many=True)
    return serializer.data[::-1]


def get_task_info_by_condition(data, username):
    condition = data.get('condition')
    print(data)
    if condition is None or len(condition) == 0:
        return get_all_task_info()
    query = Q()
    if condition['showMySelf'] is True:
        query = Q(owner=username)
        query.add(Q(reviewer=username), Q.OR)
    if condition['timeSelect'] > 0:
        time_limit = timezone.now() - timedelta(days=condition['timeSelect'])
        query.add(Q(created_time__gt=time_limit), Q.AND)
    if len(condition['statusSelect']) > 0 and -1 not in condition['statusSelect']:
        query.add((Q(status__in=condition['statusSelect'])), Q.AND)
    print(condition, query)
    tasks = Task.objects.filter(query)
    serializer = TaskListSerializer(tasks, many=True)
    print(serializer.data)
    return serializer.data[::-1]


@api_view(['POST'])
@login_required
# @permission_classes((IsAuthenticated,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def task_list(request):
    if request.user.is_authenticated is False:
        return HttpResponse('not auth', status=403)
    username = str(request.user)
    print(request.user, request.user.username)
    return JsonResponse({
        'cr_data': get_task_info_by_condition(request.data, username), 'admin': True, 'username': username}, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def add_task(request):
    print('request data:', request.data, 'request user:', request.user)

    data = request.data
    # data['owner'] = str(request.user)
    #
    # serializer = TaskListSerializer(data=data)
    # if serializer.is_valid():
    #     print('is valid, save', serializer)
    #     serializer.save()
    # else:
    #     print('not valid')

    task = Task.objects.create(
        url=data['url'],
        owner=str(request.user),
        intro=data['intro'],
    )
    task.save()

    return JsonResponse(get_task_info_by_condition(request.data, str(request.user)), safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def edit_task(request):
    print('request data:', request.data, 'request user:', request.user)

    data = request.data

    task = Task.objects.get(
        id=data['id']
    )

    if 'url' in data:
        task.url = data['url']
    if 'intro' in data:
        task.intro = data['intro']
    if 'reviewer_note' in data:
        task.reviewer_note = data['reviewer_note']
    task.save()

    return JsonResponse(get_task_info_by_condition(request.data, str(request.user)), safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def modify_task_status(request):
    data = request.data

    task = Task.objects.get(
        id=data['id']
    )
    task.status = data['status']

    if data['status'] == 2:
        task.reviewer = str(request.user)
    task.save()

    return JsonResponse(get_task_info_by_condition(request.data, str(request.user)), safe=False)


@api_view(['GET'])
def super_user(request):
    print(request.user, type(request.user))
    print(request.user.is_superuser)
    user = request.user
    print(user.username)
    print(user.password)
    # user.is_superuser = True
    # user.save()
    return JsonResponse({'success'})
