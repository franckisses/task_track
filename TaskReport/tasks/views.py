import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers
from django.db.models import Q
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

class GetTasks(View):
    @logging_check
    def get(self,request):
        user = get_user_by_request(request)
        # 普通用户只能获取自己的任务
        query_user = UserProfile.objects.filter(username=user)[0]
        role, u_id = query_user.role, query_user.id
        if role =='normal':
            ser_data = serializers.serialize('json',
                    Tasks.objects.filter(uid_id=u_id),
                    fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        elif role == 'developer':
            ser_data = serializers.serialize('json',
                    Tasks.objects.filter(Q(backend_handler=query_user.username)
                        | Q(frontend_handler=query_user.username)),
                    fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        elif role == 'admin':
            ser_data = serializers.serialize('json',Tasks.objects.all(),
                fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        data = {'code':200, 'data': ser_data}
        return JsonResponse(data)

    def update(self, request):
        pass



class ModifyTasks(View):

    @logging_check
    def post(self, request):
        pass

class OngoingTasks(View):

    @logging_check
    def get(self, request):
        user = get_user_by_request(request)
        # 普通用户只能获取自己的任务
        query_user = UserProfile.objects.filter(username=user)[0]
        role, u_id = query_user.role, query_user.id
        if role =='normal':
            ser_data = serializers.serialize('json',
                    Tasks.objects.filter(Q(uid_id=u_id) & Q(finished_rate__lt=1)),
                    fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        elif role == 'developer':
            ser_data = serializers.serialize('json',
                    Tasks.objects.filter((Q(backend_handler=query_user.username)
                        | Q(frontend_handler=query_user.username)) &
                        Q(finished_rate <1)),
                    fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        elif role == 'admin':
            ser_data = serializers.serialize('json',
                    Tasks.objects.filter(finished_rate__lt=1),
                    fields=(
                        'country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'
                    ))
        data = {'code':200, 'data': ser_data}
        return JsonResponse(data)

class FinishedTasks(View):

    @logging_check
    def get(self, request):
        user = get_user_by_request(request)
        # 普通用户只能获取自己的任务
        query_user = UserProfile.objects.filter(username=user)[0]
        role, u_id = query_user.role, query_user.id
        if role =='normal':
           ser_data = serializers.serialize('json',
                    Tasks.objects.filter(Q(uid_id=u_id) & Q(finished_rate=1)),
                    fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        elif role == 'developer':
            ser_data = serializers.serialize('json',
                    Tasks.objects.filter((Q(backend_handler=query_user.username)
                        | Q(frontend_handler=query_user.username)) &
                        Q(finished_rate =1)),
                    fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        elif role == 'admin':
            ser_data = serializers.serialize('json',Tasks.objects.filter(finished_rate=1),
                fields=('country', 'operator','created_time',
                    'task_name','deadline', 'finished_rate'))
        data = {'code':200, 'data': ser_data}
        return JsonResponse(data)

class TaskDetails(View):

    @logging_check
    def get(self, request, id):
        user = get_user_by_request(request)
        query_user = UserProfile.objects.filter(username=user)[0]
        role, u_id = query_user.role, query_user.id
        ser_data = serializers.serialize('json',
                Tasks.objects.filter(Q(uid_id=u_id) & Q(id=id))
                )
        data = {'code': 200, 'data': ser_data}
        return JsonResponse(data)
