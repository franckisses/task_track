# -*- coding: utf-8 -*-

# @Time: 2022-10-22
# @File: %
# @Author: dreamhomes
# @Description: 
from rest_framework import serializers


# 生命序列化器，所有的序列化器都是直接或者间接的继承Serializers

class TaskSerializer(serializers.Serializer):
    country = serializers.CharField()
    operator = serializers.CharField()
    priority = serializers.CharField()
    created_time = serializers.DateField()
    finished_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    task_name = serializers.CharField()
