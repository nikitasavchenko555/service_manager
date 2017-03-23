from django.conf.urls import include, url
from . import views
#from django import *
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_issue/', views.create_issue, name='create_issue'),
    url(r'^issue/(?P<number>[0-9]+)/$', views.view_issue, name='view_issue'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^view_issues_user/', views.view_issues_user, name='view_issues_user'),
    url(r'^log_user/', views.user_data, name='user_data'),
    url(r'^change_equipment_view/', views.change_equipment_view, name='change_equipment_view'),
    
]
