from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

from utils.loging_decorator import logging_check
# Create your views here.


class AddTasks(View):

    @logging_check
    def post(self, request):
        return JsonResponse({'code':200})

    def get(self,request):
        pass

    def update(self, request):
        pass



class ModifyTasks(View):

    def post(self, request):
        pass


