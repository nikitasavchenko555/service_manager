from django.shortcuts import render, redirect
from .models import *

def index(request):
    issue = issues.objects.order_by("change_date")
    return render(request, 'manager/index.html', {'issues': issue})
    
def create_issue(request):
    if request.method == "POST":
            form = IssuesForm(request.POST)
            if form.is_valid():
               issues = form.save(commit=False)
               issues.user_edit = request.user
               issues.change_date = timezone.now()
               issues.save()
            return redirect('manager.views.index')

    else:
           number = issues.objects.order_by("change_date").last() 
           forms = IssuesForm()
    return render(request, 'manager/create_issue.html', {'form': forms, 'issues': number })


    
