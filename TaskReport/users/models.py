from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=32, null=False)
    role = models.CharField(max_length=10, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['password', 'role']
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'user_profile'

