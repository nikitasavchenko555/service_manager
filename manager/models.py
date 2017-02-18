from django.db import models
from django.utils import timezone


class groups_of_reason(models.Model):
    reason = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')

class groups_of_work(models.Model):
    name = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')

class workspace(models.Model):
    name = models.CharField(max_length=300)
    change_date = models.DateTimeField('date changed')

class equipment(models.Model):
    workspace = models.ForeignKey(workspace)
    model = models.CharField(max_length=300)
    inventory_number  = models.IntegerField()
    change_date = models.DateTimeField('date changed')

    
    


    
