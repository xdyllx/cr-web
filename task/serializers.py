from rest_framework import serializers
from task.models import Task

class TaskListSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()
    created_time = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

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
            'status_display',
            'reviewer_note',
        ]

    def get_created_time(self, obj: Task):
        return obj.created_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_status_display(self, obj: Task):
        return obj.get_status_display()

    # def get_url(self, obj: Task):
    #     return 'https://www.baidu.com/'
