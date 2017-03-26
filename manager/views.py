from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from django.http import Http404
from .forms import IssuesForm, TestForm
from django.views.i18n import *
from django.contrib.auth.models import User
from login.models import *
from django.http import HttpResponse
from django.core import serializers
import re

'''def direct_login(request):
    user_warn = request.user
    if user_warn.is_authenticated:
        return redirect('index/') 
    else:
        return redirect('/login/')'''

#global cat_id
#global mod
#global inv_num
global mod_list
mod_list = []

def index(request):
    issue = issues.objects.order_by("-change_date")
    return render(request, 'manager/index.html', {'issues': issue })


def user_data(request):
        user_warn = request.user
        if user_warn.is_authenticated:
            current_user = UserProfile.objects.get(user=request.user)
        return render(request, 'manager/log_user.html', { 'current_user': current_user })

def get_model(request):
        mod_id = request.POST.get('model')

        if mod_id != None:

             mod_list.append(mod_id)
             
             t = mod_list[0]
             
             return t

        else:

             t = mod_list[0]

             return t

def get_inventory(request):
        inv = request.POST.get('num')

        if inv != None: 
            mod_list.append(inv)
            return mod_list
        else:
            t = mod_list[1]
            mod_list.clear()
            return t



            
def create_issue(request):
        new_issues = issues()
        #mod_list = []
        #inv_num_id = None
        number = issues.objects.values('number_issue').order_by().last()
        num_view = number['number_issue']+1
        form = IssuesForm()
        if request.is_ajax() == True:
             if request.method == "GET":
                    #cat_id = request.GET['name'] не работает, нужно использовать строку ниже
                cat_id = request.GET.get('name')
                if cat_id != None:
                    model = str(equipment.objects.get_model(cat_id))
                    dist = re.findall(r'[\d\w,]+', model)
                    return HttpResponse(dist)
                mod = request.GET.get('model')
                if mod != None:
                    inventory = str(equipment.objects.get_inventory(mod))
                    dist_inventory = re.findall(r'[\d\w,]+', inventory)
                    return HttpResponse(dist_inventory)
                inv_num = request.GET.get('send')
                if inv_num != None:
                     sender = str(equipment.objects.check_inventory(inv_num))
                     send_dist = re.findall(r'[\d\w,]+', sender)
                     result = "Оборудование успешно выбрано"
                     return HttpResponse(result)
             '''if request.method == "POST":
                 m = request
                 mod_id = request.POST.get('model')
                 mod_list.append(mod_id)
                 inv_num_id = request.POST.get('num')
                 mod_list.append(m)
                 return HttpResponse(mod_id)'''
        
        if request.method == "POST":
             #print(request)
             form = IssuesForm(request.POST)
             if request.is_ajax() == True:
                 mod_id = get_model(request)
                 #mod_list.append(mod_id)
                 inv_num_id = get_inventory(request)
                 #mod_list.append(inv_num_id)
             #return HttpResponse(mod_list)
             model = get_model(request)
             inventory = get_inventory(request)
             #return HttpResponse(inventory)
             if form.is_valid():
                     new_issues = form.save(commit=False)
                     new_issues.equipment_model = equipment.objects.get(model=model)
                     new_issues.equipment_inventory = equipment.objects.get(inventory_number=inventory)
                     new_issues.number_issue = num_view
                     new_issues.number_history = "1"
                     new_issues.user_edit = request.user
                     new_issues.change_date = timezone.now()
                     new_issues.save()
                     #mod_list = []
                     return redirect('/index/')
             else:
                     return  HttpResponse("Форма невалидна")
        return render(request, 'manager/create_issue.html', {'form': form, 'num_view': num_view  } )
    


def view_issue(request, number):
    try:
        issue = issues.objects.get(number_issue=number)
    except:
        raise Http404
    return render(request, 'manager/issue.html', {'issue': issue })

def view_issues_user(request):
        user_warn = request.user
        current_user = UserProfile.objects.get(user=request.user)
        issues_user = current_user
        current_user_role = str(current_user.id_state)
        if user_warn.is_authenticated:

            if current_user_role == "Координатор":
                
                issue_user = issues.objects.filter(coordinator=current_user)

            elif current_user_role == "Инициатор":
                
                issue_user = issues.objects.filter(creator=current_user)

            elif current_user_role == "Исполнитель":
                
                issue_user = issues.objects.filter(executor=current_user)

        return render(request, 'manager/issues_user.html', {'issue_user': issue_user })


'''#обработчик ajax-запроса для выбора нужного станка
def change_equipment_view(request):

        cat_id = None
        
        if request.method == "GET":
                cat_id = request.GET['name']
        message = cat_id
        model = equipment.objects.get_model(message)
        return HttpResponse(model)'''
        
     



        

        




        
   


    
