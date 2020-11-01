from django.db import models

# from django_sorcery.db import databases
# import enum
# from sqlalchemy import Enum

# db = databases.get("default")

class Results(models.Model):
    id =  models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255,  null=True)
    timestamp = models.DateField()
    task_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=NOT_STARTED)
    #task_status = models.Column(Enum(TaskStatus))
    http_status = models.IntegerField(default=200)
