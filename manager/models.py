from django.db import models
from django import forms
from django.utils import timezone
from datetime import datetime 
from django.contrib.auth.models import User
from django.forms import ModelForm, inlineformset_factory
from django.utils.safestring import mark_safe
from login.models import *
from django.db import connection

def uknown_user():
    id = 777
    return id

class equipment_manager(models.Manager):
     def get_name(self, workspace):
         #from django.db import connection
         cursor = connection.cursor()
         cursor.execute("""
            SELECT DISTINCT e.name
            FROM manager_equipment e
            where e.workspace_id=%s""", [workspace])
         result_list = [row for row in cursor.fetchall()]

         def __str__(self):

              return self.name 
        
         return result_list

     def get_model(self, message):
         #from django.db import connection
         cursor = connection.cursor()
         cursor.execute("""
            SELECT e.model
            FROM manager_equipment e 
            where e.name=%s""", [message])
         cursor_list = cursor.fetchall()
         model_list = [ row for row in cursor_list ]
        
         return model_list

     def get_inventory(self, model):
         #from django.db import connection
         cursor = connection.cursor()
         cursor.execute("""
            SELECT e.inventory_number
            FROM manager_equipment e
            where e.model=%s""", [model])
         inventory_list = [row for row in cursor.fetchall()]
        
         return inventory_list
     
     def check_inventory(self, inv):
         #from django.db import connection
         cursor = connection.cursor()
         cursor.execute("""
            SELECT e.inventory_number
            FROM manager_equipment e
            where e.inventory_number=%s""", [inv])
         check_list = [row for row in cursor.fetchall()]
        
         return check_list

     def get_report(self, start_period_result, end_period_result):
         #from django.db import connection
         cursor = connection.cursor()
         cursor.execute("""select * from issues_report_2 i
where i.start_down_date between (timestamp %s)::date and (timestamp %s)::date""", [start_period_result, end_period_result])
         result_report = [row for row in cursor.fetchall()]

         def __str__(self):

              return self.name 
        
         return result_report

     def get_source(self, search):
         #from django.db import connection
         cursor = connection.cursor()
         search_right = '%'+search+'%' 
         cursor.execute("""select il.number_issue, il.level_issue_id, il.status, mi.brief_description, au.username as creator, il.coordinator
from issues_report_2 il, manager_issues mi, auth_user au, login_userprofile lu
where mi.number_issue = il.number_issue
and mi.creator_id = lu.id
and lu.user_id = au.id
and ((il.name like %s) or (il.number_issue::text like %s) or (il.model like %s) or (il.status like %s) or(il.name_equipment like %s) or (il.inventory_number::text like %s) or (il.coordinator like %s))""", [search_right, search_right, search_right, search_right, search_right, search_right, search_right])
         result_source = cursor.fetchall()#[row for row in cursor.fetchall()]

         def __str__(self):

              return self.name 
        
         return result_source


     def get_number(self, number):
         cursor = connection.cursor()
         cursor.execute("""select il.number_issue, il.level_issue_id, il.status, mi.brief_description, au.username as creator, il.coordinator
from issues_report_2 il, manager_issues mi, auth_user au, login_userprofile lu
where mi.number_issue = il.number_issue
and mi.creator_id = lu.id
and lu.user_id = au.id
and il.number_issue =%s;""", [number])
         result_number = [row for row in cursor.fetchall()]

         def __str__(self):

              return self.name 
        
         return result_number

     def get_stat_level_issue(self, start_period, end_period):
         cursor = connection.cursor()
         cursor.execute("""select mli.level, count(mi.*) from manager_issues mi, manager_level_issue mli
where mi.level_issue_id  = mli.id and mi.start_down_date between (timestamp %s)::date and (timestamp %s)::date group by mli.level""", [start_period, end_period])
         result_stat = [row for row in cursor.fetchall()]
        
         return result_stat


     def get_stat_downtime(self, start_period, end_period, workspace_id, model, inventory_number):
         cursor = connection.cursor()
         cursor.execute("""select w.name, e.model, e.inventory_number , mi.* from manager_issues mi, manager_equipment e, manager_workspace w
where mi.equipment_model_id  = e.id
and e.workspace_id = w.id
and mi.start_down_date between (timestamp %s)::date and (timestamp %s)::date
and w.id = %s
and e.model = %s
and e.inventory_number = %s""", [start_period, end_period, workspace_id, model, inventory_number])
         result_stat = [row for row in cursor.fetchall()]
        
         return result_stat


     


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
    description = models.CharField(max_length=200)
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    class Meta:
        verbose_name = 'Словарь статусов сотрудников'
        verbose_name_plural = 'Словари статусов сотрудников'
    def __str__(self):
        return self.description




   

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
    model = models.CharField(max_length=20, unique=True)
    inventory_number  = models.IntegerField()
    change_date = models.DateTimeField(default = timezone.now)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    objects = equipment_manager()
    class Meta:
        verbose_name = 'Список оборудования'
        verbose_name_plural = 'Списки оборудования'

    
    def __str__(self):

        return self.name

    def test_method(self):

        return str(self.model)




class issues(models.Model):
    
    number_issue = models.IntegerField(primary_key=True)
    level_issue = models.ForeignKey(level_issue)
    current_status = models.ForeignKey(status_issue)
    brief_description = models.CharField(max_length=200)
    start_down_date = models.DateField()
    start_down_time = models.TimeField()
    start_issue_date = models.DateField()
    start_issue_time = models.TimeField()
    workspace = models.ForeignKey(workspace)
    equipment_name = models.ForeignKey(equipment, verbose_name="Тип", related_name='+')
    equipment_model = models.ForeignKey(equipment, verbose_name="Модель", related_name='+')
    equipment_inventory = models.ForeignKey(equipment, verbose_name="Инвентарный №", related_name='+')
    creator = models.ForeignKey('login.UserProfile', verbose_name="Инициатор", related_name="issue_creator")
    groups_of_work = models.ForeignKey(groups_of_work)
    coordinator = models.ForeignKey('login.UserProfile', verbose_name="Координатор", related_name="issue_coordinator")
    executor = models.ForeignKey('login.UserProfile', verbose_name="Исполнитель", related_name="issue_executor")
    progress = models.CharField(max_length=1000)
    group_of_reason = models.ForeignKey(groups_of_reason, blank=True)
    solution = models.ForeignKey(solutions, blank=True)
    number_history = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    change_date = models.DateTimeField(default = timezone.now)
    close_down_date = models.DateField(blank=True, null=True)
    close_down_time = models.TimeField(blank=True, null=True)
    close_issue_date = models.DateField(blank=True, null=True)
    close_issue_time = models.TimeField(blank=True, null=True)
    user_edit = models.ForeignKey('auth.User', default=uknown_user)
    #issue_objects = IssueManager()
    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'


class Reports(models.Model):
    creator = models.ForeignKey('auth.User')
    report = models.FileField(upload_to = "report/")
    
    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'










    
