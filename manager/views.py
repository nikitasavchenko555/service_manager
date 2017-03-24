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


def index(request):
    issue = issues.objects.order_by("-change_date")
    return render(request, 'manager/index.html', {'issues': issue })


def user_data(request):
        user_warn = request.user
        if user_warn.is_authenticated:
            current_user = UserProfile.objects.get(user=request.user)
        return render(request, 'manager/log_user.html', { 'current_user': current_user })

def equipment_data(name, model, inventory):
        name_1 = name
        model_1 = model
        inventory_1 = inventory
def create_issue(request):
        #global new_issues
        new_issues = issues()
        number = issues.objects.values('number_issue').order_by().last()
        num_view = number['number_issue']+1
        form = IssuesForm()
        #global cat_id
        #global mod
        #global inv_num
        cat_id = None
        mod = None
        inv_num = None
        #new = equipment_data(cat_id)
        if request.is_ajax() == True: 
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
                             #dist_inv = "Успешно"
                             return HttpResponse(dist_inventory)
                    inv_num = request.GET.get('send')
                    if inv_num != None:
                         sender = str(equipment.objects.check_inventory(inv_num))
                         send_dist = re.findall(r'[\d\w,]+', sender)
                         result = "Оборудование успешно добавлено"
                         return HttpResponse(result)
                                     
        #if request.is_ajax() == True: 
        if request.method == "POST":
             form = IssuesForm(request.POST)
            #if request.is_ajax() == True:
             cat_id = request.POST.get('cat_id')
             mod = request.POST.get('model')
             inv_num = request.POST.get('num')
             #new = equipment_data(cat_id)
             if cat_id != None and mod != None and inv_num != None:
                      return HttpResponse(mod)
             #name_id = new
            #if form.is_valid():
             #new_issues = form.save(commit=False)
            #new_issues.equipment_name_id = cat_id
             new_issues.equipment_model = mod
             new_issues.equipment_inventory_id = inv_num
             new_issues.number_issue = num_view
             new_issues.number_history = "1"
             new_issues.user_edit = request.user
             new_issues.change_date = timezone.now()
                
                      #form = IssuesForm(request.POST)
             if form.is_valid():
                      new_issues.equipment_inventory_id = inv_num
                      new_issues.save()
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
        
     



        

        




        
   


    
