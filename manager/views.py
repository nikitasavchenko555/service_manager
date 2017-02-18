from django.shortcuts import render

def index(request):
    return render(request, 'manager/index.html', {})
def create_issue(request):
    return render(request, 'manager/create_issue.html', {})
    
