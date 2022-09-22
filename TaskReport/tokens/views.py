import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def tokens(request):
    if request =='POST':
        print(request.body)
        return JsonResponse({'status':200})
    return JsonResponse({'status':300, 'error': 'shit'})
