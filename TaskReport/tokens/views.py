import hashlib
import json
import time
from django.utils import timezone
# from carts.utils import *
from django.http import JsonResponse
from users.models import UserProfile

from utils.loging_decorator import get_user_by_request

# Create your views here.
def tokens(request):
    '''
    创建token == 登录
    :param request:
    :return:
    '''
    if not request.method == 'POST':
        result = {'code': 101 , 'error': 'Please use POST'}
        return JsonResponse(result)
    #前端地址 http://127.0.0.1:5000/login
    #获取前端传来的数据/生成token
    #获取-校验密码-生成token
    #获取前端提交的数据
    json_str = request.body
    if not json_str:
        result = {'code': 102, 'error': 'Please give me json'}
        return JsonResponse(result)

    json_obj = json.loads(json_str)
    username = json_obj.get('username')
    password = json_obj.get('password')
    if not username:
        result = {'code':103, 'error': 'Please give me username'}
        return JsonResponse(result)
    if not password:
        result = {'code':104, 'error': 'Please give me password'}
        return JsonResponse(result)

    #####校验数据#####
    user = UserProfile.objects.filter(username=username)
    if not user:
        result = {'code':105, 'error': 'username or password is wrong !! '}
        return JsonResponse(result)

    user = user[0]
    if password != user.password:
        result = {'code': 106, 'error': 'username or password is wrong'}
        return JsonResponse(result)
    #make token
    user.last_login = timezone.now()
    user.save()
    role = user.role
    token = make_token(username)
    result = {'code':200, 'role': role, 'username':username, 'data':{'token':token}}
    # 前端会有
    return JsonResponse(result)




def make_token(username, expire=3600 * 24):
    # 官方jwt / 自定义jwt
    import jwt
    key = '1234567'
    now = time.time()
    payload = {'username': username, 'exp': int(now + expire)}
    return jwt.encode(payload, key, algorithm='HS256')


def refresh_token(request):
    if request.method == 'GET':
        if get_user_by_request(request):
            result = {'code':200, 'data': 'token still alive'}
            return JsonResponse(result)
        else:
            result ={'code':107, 'error': 'please relogin '}
            return JsonResponse(result)

