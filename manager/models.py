from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager

def uknown_user():
    id = 777
    return id


class groups_of_reason(models.Model): #группы причин
    reason = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User')

class solutions(models.Model):#способ устранения
    reason = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    

class groups_of_work(models.Model): #cписок рабочих групп
    name = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)

class level_issue(models.Model): #уровни инцидентов
    level = models.IntegerField()
    description = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)

class status_issue(models.Model): #статус инцидентов
    status = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    

class State(models.Model):#словарь статусов сотрудников
    id_state = models.PositiveSmallIntegerField()
    description_state = models.CharField(max_length=200)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)


class workers(models.Model): #список сотрудников
    position = models.CharField(max_length=200)
    fio = models.CharField(max_length=200)
    id_state = models.ForeignKey(State)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
   

class workspace(models.Model): #список подразделений
    name = models.CharField(max_length=300)
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)

class equipment(models.Model): #список оборудования
    workspace = models.ForeignKey(workspace)
    model = models.CharField(max_length=300)
    inventory_number  = models.IntegerField()
    change_date = models.DateTimeField('date changed')
    user_edit = models.ForeignKey('auth.User', default=uknown_user)

class issue(models.Model):
    number_issue = models.IntegerField(primary_key=True)
    number_history = models.IntegerField()
    status = models.ForeignKey(status_issue)
    brief_description = models.CharField(max_length=200)
    start_downtime = models.DateTimeField()
    start_issue = models.DateTimeField()
    workspace = models.ForeignKey(workspace)
    equipment = models.ForeignKey(equipment)
    creator = models.ForeignKey(workers, verbose_name="Инициатор", related_name="issue_creator")
    groups_of_work = models.ForeignKey(groups_of_work)
    coordinator = models.ForeignKey(workers, verbose_name="Координатор", related_name="issue_coordinator")
    executor = models.ForeignKey(workers, verbose_name="Исполнитель", related_name="issue_executor")
    progress = models.CharField(max_length=1000)
    reason = models.ForeignKey(groups_of_reason)
    reason = models.ForeignKey(solutions)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    
    
    
    
    


    
