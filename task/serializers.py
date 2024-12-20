from rest_framework import serializers
from task.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'url',
            'owner',
            'intro',
            'created_time',
            'reviewer',
            'status',
        ]

    # def get_url(self, obj: Task):
    #     return 'https://www.baidu.com/'
