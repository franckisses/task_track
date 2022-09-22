import json

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def register(request):
    if request.method =='POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username, password)
        return JsonResponse({'status': 200})
    elif request.method == 'GET':
        return JsonResponse({'status': 200})

