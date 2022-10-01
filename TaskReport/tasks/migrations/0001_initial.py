# Generated by Django 3.2.15 on 2022-10-01 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=32)),
                ('operator', models.CharField(max_length=32)),
                ('priority', models.CharField(max_length=3)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('backend_handler', models.CharField(max_length=20, verbose_name='后段处理人')),
                ('frontend_handler', models.CharField(max_length=20, verbose_name='前端处理人')),
                ('backend_finished_rate', models.FloatField(verbose_name='后段完成度')),
                ('frontend_finished_rate', models.FloatField(verbose_name='前段完成度')),
                ('finished_rate', models.FloatField(verbose_name='完成度')),
                ('deadline', models.DateField(verbose_name='最后期限')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'all_tasks',
            },
        ),
    ]
