from django.db import models
from uuid import uuid4


class AccessToken(models.Model):
    token = models.CharField(max_length=100,default=uuid4)
    name = models.CharField(max_length=50)
    description = models.TextField()

class UserKeys(models.Model):
    username = models.CharField(max_length=200)
    secret = models.CharField(max_length=200,default=uuid4)
    key = models.CharField(max_length=200,default=uuid4)
    account_id = models.IntegerField(default=100000)