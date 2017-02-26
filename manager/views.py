from django.shortcuts import render
from .models import *

def index(request):
    issue = issues.objects.order_by("change_date")
    return render(request, 'manager/index.html', {'issues': issue})
    
def create_issue(request):
    levels = level_issue.objects.order_by("level")
    return render(request, 'manager/create_issue.html', {'level_issue': levels})


    
