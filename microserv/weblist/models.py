from django.db import models

class Results(models.Model):
    address = models.CharField(max_length=255,  null=True)
    words_count = models.IntegerField(null=True)
    http_status_code = models.IntegerField()

class TaskPars(models.Model):
    NOT_STARTED = 1
    PENDING = 2
    FINISHED = 3
    STATUS_CHOICES = (
        (NOT_STARTED, 'NOT_STARTED'),
        (PENDING, 'PENDING'),
        (FINISHED, 'FINISHED'),
    )
    address = models.CharField(max_length=255,  null=True)
    timestamp = models.DateTimeField()
    task_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=NOT_STARTED)
    http_status = models.IntegerField(default=200)
