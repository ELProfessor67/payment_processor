from django.db import models
import datetime
# Create your models here.

class Batchs(models.Model):
    owner = models.CharField(max_length=100)
    batch_id = models.IntegerField(default=1)
    name = models.CharField(max_length=50)
    desciption = models.CharField(max_length=300)
    username = models.CharField(max_length=100)
    transactions = models.CharField(max_length=50000000,default='[]')
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=50,default="Pending")