from django.db import models
from uuid import uuid4


class AccessToken(models.Model):
    token = models.CharField(max_length=100,default=uuid4)
    name = models.CharField(max_length=50)
    description = models.TextField()