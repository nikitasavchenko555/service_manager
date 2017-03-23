from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from django.http import Http404
from .forms import IssuesForm, TestForm
from django.views.i18n import *
from django.contrib.auth.models import User
from login.models import *
from django.http import HttpResponse
from django.core import serializers




def index(request):
    issue = issues.objects.order_by("-change_date")
    return render(request, 'manager/index.html', {'issues': issue })


def user_data(request):
        user_warn = request.user
        if user_warn.is_authenticated:
            current_user = UserProfile.objects.get(user=request.user)
        return render(request, 'manager/log_user.html', { 'current_user': current_user })

    
def create_issue(request):
        new_issues = issues()
        number = issues.objects.values('number_issue').order_by().last()
        equipment_name = equipment.objects.get_name()
        num_view = number['number_issue']+1
        form = IssuesForm()
        
        if request.method == "POST":
            form = IssuesForm(request.POST)
            #name_in = name(request.POST)
            if form.is_valid():
                   new_issues = form.save(commit=False)
                   new_issues.number_issue = num_view
                   new_issues.number_history = "1"
                   new_issues.user_edit = request.user
                   new_issues.change_date = timezone.now()
                   new_issues.save()
                   return redirect('/index/')
            else:
                return  HttpResponse("Форма невалидна")
        return render(request, 'manager/create_issue.html', {'form': form, 'num_view': num_view, 'equipment_name': equipment_name   } )
    


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



def change_equipment_view(request):

        cat_id = None
        if request.is_ajax():
            if request.method == "GET":
                cat_id = request.POST.get('name')
                message = "Получилось"
            return HttpResponse(message)
        
     


'''def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('ok', content_type='text/html')
        else:
            return HttpResponse('неверный логин/пароль!', content_type='text/html')
    else:
        return HttpResponse('Ошибка авторизации!', content_type='text/html')'''
        

        




        
   


    
