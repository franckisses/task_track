import json

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def register(request):
    if request.method =='POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not (username and password):
            result = {'status': 10001, error: 'username or password error!'}
        
        print(username, password)
        return JsonResponse({'status': 200})
    elif request.method == 'GET':
        return JsonResponse({'status': 200})

