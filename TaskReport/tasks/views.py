import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

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
        task_desc = data.get('task_doc')
        files = data.get('files')
        for key, value in data.items():
            print(key, '-->', value)
        return JsonResponse({'code':200})

    def get(self,request):
        pass

    def update(self, request):
        pass



class ModifyTasks(View):

    def post(self, request):
        pass


