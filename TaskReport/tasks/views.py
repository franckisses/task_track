import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers

from .models import Tasks
from users.models import UserProfile
from utils.loging_decorator import logging_check, get_user_by_request
# Create your views here.


class AddTasks(View):

    @logging_check
    def post(self, request):
        data = json.loads(request.body)
        user = get_user_by_request(request)
        if not user:
            data = {'code': 403, 'error': 'please login again!'}
            return JsonResponse(data)
        project_country = data.get('project_country')
        customer_name = data.get('customer_name')
        task_name = data.get('task_name')
        task_desc = data.get('task_desc')
        deadline = data.get('deadline')
        # save 
        new_tasks = Tasks(
                uid=user,
                country=project_country,
                operator=customer_name,
                task_name = task_name,
                task_desc = task_desc,
                backend_finished_rate=0,
                frontend_finished_rate=0,
                finished_rate=0,
                deadline=deadline
                )

        new_tasks.save()
        return JsonResponse({'code':200})

class Tasks(View):
    @logging_check
    def get(self,request):
        user = get_user_by_request(request)
        # 普通用户只能获取自己的任务
        if user.role =='normal':
            Users = UserProfile.objects.filter(username=user)
            print(Users.id)
            data = Users.Tasks_set().all()
            print(data)
            pass
        elif user.role == 'developer':
            pass
        elif user.role == 'admin':
            pass

    def update(self, request):
        pass



class ModifyTasks(View):

    def post(self, request):
        pass


