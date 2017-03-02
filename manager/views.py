from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from django.http import Http404
from .forms import IssuesForm


def index(request):
    issue = issues.objects.order_by("change_date")
    return render(request, 'manager/index.html', {'issues': issue})
    
def create_issue(request):
    #try:
        if request.method == "POST":
            form = IssuesForm(request.POST)
            if form.is_valid():
                   issues = form.save(commit=False)
                   issues.number_history = "1"
                   issues.user_edit = request.user
                   issues.change_date = timezone.now()
                   issues.save()
                   return redirect('/index/')
            #else:
                #return  HttpResponse("Форма невалидна")
        else:
           #number = issues.objects.order_by("change_date").last() 
            form = IssuesForm()
        return render(request, 'manager/create_issue.html', {'form': form })
    #except:
       # return  HttpResponse("У нас проблема")


def view_issue(request, number):
    try:
        issue = issues.objects.get(number_issue=number)
    except:
        raise Http404
    return render(request, 'manager/issue.html', {'issue': issue })
   


    
