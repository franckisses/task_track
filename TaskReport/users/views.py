import json

from django.shortcuts import render
from django.http import JsonResponse

from .models import UserProfile
# Create your views here.
import traceback


def register(request):
    if request.method =='POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not (username and password):
            result = {'code': 10001, 'error': 'username or password error!'}

        # check user exists or not
        users = UserProfile.objects.filter(username=username)
        if users:
            result = {'code':10004, 'error':'username already eixsts!'}
            return JsonResponse(result)
        try:
            user = UserProfile.objects.create(
                    username=username,
                    password=password,
                    role='normal'
                    )
            user.save()
        except Exception as e:
            print(e)
            result = {'code': 10002, 'error': 'create user failed'}
            return JsonResponse(result)
        else:
            result = {'code': 200, 'data':{'message':'success'}}
            return JsonResponse(result)
    elif request.method == 'GET':
        result = {'code':10003, 'error':'illegal request'}
        return JsonResponse(result)

