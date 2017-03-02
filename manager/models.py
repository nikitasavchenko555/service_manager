from django.db import models
from django import forms
from django.utils import timezone
from datetime import datetime 
from django.contrib.auth.models import User
from django.forms import ModelForm, inlineformset_factory
#надо исправить возможность задавать null в поле level_issue

def uknown_user():
    id = 777
    return id


class groups_of_reason(models.Model): #группы причин
    reason = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User')
    class Meta:
        verbose_name = 'Группа причин'
        verbose_name_plural = 'Группы причин'
    def __str__(self):
        return self.reason


class solutions(models.Model):#способ устранения
    reason = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Способ устранения'
        verbose_name_plural = 'Способы устранения'
    def __str__(self):
        return self.reason


class groups_of_work(models.Model): #cписок рабочих групп
    name = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Список рабочих групп'
        verbose_name_plural = 'Списки рабочих групп'
    def __str__(self):
        return self.name
   

class level_issue(models.Model): #уровни инцидентов
    level = models.IntegerField()
    description = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Уровень инцидента'
        verbose_name_plural = 'Уровни инцидентов'
    def __str__(self):
        return '%d' % (self.level)

class status_issue(models.Model): #статус инцидентов
    status = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Статус инцидентов'
        verbose_name_plural = 'Статусы инцидентов'
    def __str__(self):
        return self.status
    

class State(models.Model):#словарь статусов сотрудников
    id_state = models.PositiveSmallIntegerField()
    description_state = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Словарь статусов сотрудников'
        verbose_name_plural = 'Словари статусов сотрудников'
    def __str__(self):
        return self.description_state


class workers(models.Model): #список сотрудников
    position = models.CharField(max_length=200)
    fio = models.CharField(max_length=200)
    id_state = models.ForeignKey(State)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Список сотрудников'
        verbose_name_plural = 'Списки сотрудников'
    def __str__(self):
        return self.fio

   

class workspace(models.Model): #список подразделений
    name = models.CharField(max_length=300)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Список подразделений'
        verbose_name_plural = 'Списки подразделений'
    def __str__(self):
        return self.name
    

class equipment(models.Model): #список оборудования
    workspace = models.ForeignKey(workspace)
    name = models.CharField(max_length=300)
    model = models.CharField(max_length=20)
    inventory_number  = models.IntegerField()
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Список оборудования'
        verbose_name_plural = 'Списки оборудования'
    def __str__(self):
        return (self.name)

class issues(models.Model):
    number_issue = models.IntegerField(primary_key=True)
    level_issue = models.ForeignKey(level_issue)
    current_status = models.ForeignKey(status_issue)
    brief_description = models.CharField(max_length=200)
    start_downtime = models.DateTimeField()
    start_issue = models.DateTimeField()
    workspace = models.ForeignKey(workspace)
    equipment_name = models.ForeignKey(equipment, verbose_name="Тип", related_name="equipment_name")
    equipment_model = models.ForeignKey(equipment, verbose_name="Модель", related_name="equipment_model")
    equipment_inventory = models.ForeignKey(equipment, verbose_name="Инвентарный №", related_name="equipment_inventory")
    creator = models.ForeignKey(workers, verbose_name="Инициатор", related_name="issue_creator")
    groups_of_work = models.ForeignKey(groups_of_work)
    coordinator = models.ForeignKey(workers, verbose_name="Координатор", related_name="issue_coordinator")
    executor = models.ForeignKey(workers, verbose_name="Исполнитель", related_name="issue_executor")
    progress = models.CharField(max_length=1000)
    group_of_reason = models.ForeignKey(groups_of_reason, blank=True)
    solution = models.ForeignKey(solutions, blank=True)
    number_history = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'



'''class IssuesForm(ModelForm):
     class Meta:
         model = issues
         fields = ['number_issue', 'level_issue', 'current_status', 'brief_description', 'start_downtime', 'start_issue',
 'workspace', 'equipment_name', 'equipment_model', 'equipment_inventory', 'creator', 'groups_of_work', 'coordinator', 'executor', 'progress', 'group_of_reason', 'solution', 'comment']
         widgets = {'progress': forms.Textarea, 'brief_description': forms.Textarea,'start_downtime':forms.SplitDateTimeWidget}

IssuesFormSet = inlineformset_factory(equipment, issues, fk_name=('equipment_name'), form=IssuesForm)'''
         
    
    
    
    
    
    


    
