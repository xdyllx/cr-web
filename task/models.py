from django.db import models
import datetime
from django.utils import timezone


class Task(models.Model):
    # 标题
    url = models.CharField(max_length=200)
    # owner
    owner = models.CharField(max_length=30)
    intro = models.CharField(max_length=100, default='')

    created_time = models.DateTimeField(default=timezone.now)

    reviewer = models.CharField(max_length=30, blank=True)

    status_choices = (
        (1, '待处理'),
        (2, '进行中'),
        (3, '已通过'),
        (4, '已驳回'),
        (5, '已废弃'),
    )

    # 1 待处理 2 进行中 3 已完成 4 已废弃
    status = models.SmallIntegerField(default=1, choices=status_choices)

    reviewer_note = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.url + ' ' + self.owner
