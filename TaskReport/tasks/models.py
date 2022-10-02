from django.db import models
from users.models import UserProfile

# Create your models here.


class Tasks(models.Model):
    uid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    country = models.CharField(max_length=32)
    operator = models.CharField(max_length=32)
    priority = models.CharField(max_length=3) # High or Low 
    created_time = models.DateField(auto_now_add=True)
    backend_handler = models.CharField(max_length=20, verbose_name='后段处理人')
    frontend_handler = models.CharField(max_length=20, verbose_name='前端处理人')
    backend_finished_rate = models.FloatField(verbose_name='后段完成度')
    frontend_finished_rate = models.FloatField(verbose_name='前段完成度')
    finished_rate = models.FloatField(verbose_name='完成度')
    deadline = models.DateField(auto_now=False,auto_now_add=False,verbose_name='最后期限')

    class Meta:
        db_table = 'all_tasks'

class TaskFile(models.Model):
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=150,null=False)
