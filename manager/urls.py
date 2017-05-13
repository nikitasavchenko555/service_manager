from django.conf.urls import include, url
from . import views
#from django import *
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    #url(r'^$', views.direct_login, name='direct_login'),
    url(r'^$', views.index, name='index'),
    url(r'^create_issue/', views.create_issue, name='create_issue'),
    url(r'^issue/(?P<number>[0-9]+)/$', views.view_issue, name='view_issue'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^view_issues_user/', views.view_issues_user, name='view_issues_user'),
    url(r'^view_issues_wait/', views.view_issues_user_wait, name='view_issues_user_wait'),
    url(r'^log_user/', views.user_data, name='user_data'), 
    url(r'^view_issues_groups/', views.view_issues_user_groups, name='view_issues_user_groups'),
    url(r'^issue_edit/(?P<number>[0-9]+)/$', views.issue_edit, name='issue_edit'),
    url(r'^reports/', views.view_reports, name='view_reports'),
    #url(r'^reports/manager+', views.upload_report, name='upload_report'),
    
]
