# Generated by Django 3.2.15 on 2022-10-15 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_taskfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
